import pathlib
import subprocess
import io
import re

from isort import SortImports
from aiohttp import web

from app.models import Project
from app.core import get_todos
from app.core.fetch_html5_tags import get_html5_tags_set
from app.core.vue_template_parser import get_list_of_used_rags


async def get_file_todos(request):
    data = await request.json()
    id = data['project_id']
    file_abs_path = data['path']

    path = await Project.get_path(request, id)
    todos_num, todos = get_todos(file_abs_path, path)

    return web.json_response({'todos': todos, 'todos_num': todos_num}, status=200)


async def get_vue_file_hierarchy(request):
    data = await request.json()
    id = data['project_id']
    file_abs_path = data['path']

    path = await Project.get_path(request, id)
    code = pathlib.Path(file_abs_path).read_text()
    rex = re.compile(r'<template.*?>.*?</template>',re.MULTILINE|re.DOTALL)
    match = rex.match(code)
    template = match.group()
    html5_tags = get_html5_tags_set()
    used_tags = get_list_of_used_rags(template)
    retTags = [{'name':tag} for tag in used_tags if tag not in html5_tags and not tag.startswith('v-')]

    return web.json_response({'tags': retTags}, status=200)


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
