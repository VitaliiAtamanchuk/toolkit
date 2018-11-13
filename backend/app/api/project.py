from aiohttp import web

async def get_stat(request):
    return web.json_response({
        't': request.match_info['id']
    })
