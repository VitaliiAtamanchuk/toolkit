from aiohttp import web
from git.exc import NoSuchPathError

from app.models import Project
from app.core import get_tree, get_stats, get_all_todos


async def project_create(request):
    data = await request.json()
    await Project.create(request, data['path'])
    return web.json_response({}, status=201)


async def project_list(request):
    retval = await Project.all(request)
    return web.json_response({
        'list': retval
    })


async def project_delete(request):
    id = request.match_info['id']
    await Project.delete(request, id)
    return web.json_response({})


async def project_tree(request):
    id = request.match_info['id']
    path = await Project.get_path(request, id)

    try:
        import time
        start_time = time.time()
        project_tree = get_tree(path)
        print("--- %s seconds ---" % (time.time() - start_time))
    except FileNotFoundError:
        return web.json_response({}, status=400)
    else:
        return web.json_response({
            'tree': project_tree
        })


async def project_stats(request):
    id = request.match_info['id']
    path = await Project.get_path(request, id)

    try:
        import time
        start_time = time.time()
        stats = get_stats(path)
        print("--- %s seconds ---" % (time.time() - start_time))
    except NoSuchPathError:
        return web.json_response({}, status=400)
    else:
        return web.json_response({
            'stats': stats
        })

async def get_project_todos(request):
    id = request.match_info['id']
    path = await Project.get_path(request, id)

    try:
        import time
        start_time = time.time()
        todos, authors = get_all_todos(path)
        print("--- %s seconds ---" % (time.time() - start_time))
    except NoSuchPathError:
        return web.json_response({}, status=400)
    else:
        return web.json_response({
            'todos': todos,
            'authors': authors
        })