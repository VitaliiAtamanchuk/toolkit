import pathlib
import sys

from aiohttp import web


async def explore(request):
    data = await request.json()
    currPath = pathlib.Path(data['path'])
    try:
        retDirs = [_dir.name for _dir in currPath.iterdir() if _dir.is_dir()]
    except FileNotFoundError:
        return web.json_response({}, status=400)
    else:
        return web.json_response({
            'dirs': retDirs
        })

