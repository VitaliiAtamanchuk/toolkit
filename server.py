from aiohttp import web

from main import get_tree


async def get_project_view(request):
  retval = get_tree()
  return web.json_response(retval)


def init():
  app = web.Application()
  app.router.add_get('/project/read', get_project_view)
  return app


web.run_app(init(), port=8001)