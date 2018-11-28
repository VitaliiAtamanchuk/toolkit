import pathlib
import subprocess
import io

from isort import SortImports
from aiohttp import web

from app.models import Project
from app.core import get_todos


async def get_file_todos(request):
    data = await request.json()
    id = data['project_id']
    file_abs_path = data['path']

    path = await Project.get_path(request, id)
    todos_num, todos = get_todos(file_abs_path, path)

    return web.json_response({'todos': todos, 'todos_num': todos_num}, status=200)


async def py_mccabe(request):
    data = await request.json()

    # TODO: windows OS compatible
    cmd = ['python', '-m', 'mccabe', '--min', str(data['complexity']), data['path']]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    lines = []
    while True:
        line = proc.stdout.readline()
        if line != b'':
            lines.append(line.decode("utf-8"))
        else:
            break
    return web.json_response({'lines': lines}, status=200)


async def py_isort_diff(request):
    data = await request.json()

    # TODO: windows OS compatible
    cmd = ['python', './app/subprocess/isort_diff.py', data['path']]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    lines = []
    while True:
        line = proc.stdout.readline()
        if line != b'':
            lines.append(line.decode("utf-8"))
        else:
            break
    return web.json_response({'lines': lines}, status=200)


async def py_isort_fix(request):
    data = await request.json()
    SortImports(data['path'])
    return web.json_response({}, status=200)
