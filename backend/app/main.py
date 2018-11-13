import base64
from pathlib import Path

import aiohttp_jinja2
import jinja2
from aiohttp import web

import aiohttp_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiopg.sa import create_engine
from sqlalchemy.engine.url import URL

from .settings import Settings
from .views import index, message_data, messages


THIS_DIR = Path(__file__).parent
BASE_DIR = THIS_DIR.parent


def pg_dsn(settings: Settings) -> str:
    """
    :param settings: settings including connection settings
    :return: DSN url suitable for sqlalchemy and aiopg.
    """
    return str(URL(
        database=settings.DB_NAME,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        username=settings.DB_USER,
        drivername='postgres',
    ))


async def startup(app: web.Application):
    app['pg_engine'] = await create_engine(pg_dsn(app['settings']), loop=app.loop)


async def cleanup(app: web.Application):
    app['pg_engine'].close()
    await app['pg_engine'].wait_closed()


def setup_routes(app):
    from .routes import routers
    for router in routers:
        app.router.add_route(router[0], router[1], router[2])
    # app.router.add_get('/', index, name='index')
    # app.router.add_route('*', '/messages', messages, name='messages')
    # app.router.add_get('/messages/data', message_data, name='message-data')
    app.router.add_static('/static/', 'static/', name='static')


async def create_app():
    app = web.Application()
    settings = Settings()
    app.update(
        name='backend',
        settings=settings
    )

    jinja2_loader = jinja2.FileSystemLoader(str(THIS_DIR / 'templates'))
    aiohttp_jinja2.setup(app, loader=jinja2_loader)
    app['static_root_url'] = '/static'

    app.on_startup.append(startup)
    app.on_cleanup.append(cleanup)

    secret_key = base64.urlsafe_b64decode(settings.COOKIE_SECRET)
    aiohttp_session.setup(app, EncryptedCookieStorage(secret_key))

    setup_routes(app)
    return app
