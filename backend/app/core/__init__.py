import pathlib
import json
import mmap
from datetime import datetime
import re

from git import Repo
import git.exc
import aiofiles


FILES_TO_SKIP = ['.svg', '.png', '.ico', '.lock', '.log', '.jpg', '.PNG']
FILEEXTS_TO_INCLUDE = ['.py', '.js', '.vue', '.spec', '.c', '.css',
  '.html', '.mako', '.sass', '.scss', '.cpp']
FILES_REGEX_TO_SKIP_ATGITSTATS = [r'_generated.py', r'alembic_default/versions']


def get_all_todos(_path, project_path=None, _cache={}):
  # if (_path, project_path) in _cache:
  #   return _cache[(_path, project_path)]
  if project_path is None:
    project_path = _path
  path = pathlib.Path(_path)
  retval = []
  authors = {None}
  for curFile in path.iterdir():
    # TODO: list of regex to skip.
    if curFile.name.startswith('.') \
      or curFile.name == 'node_modules'\
      or curFile.name == 'public'\
      or curFile.name == 'htmlcov'\
      or curFile.name == '__pycache__':
      continue
    abs_path = str(curFile.resolve())
    if curFile.is_dir():
      vals, _authors = get_all_todos(abs_path, project_path)
      retval += vals
      authors.update(_authors)
    else:
      if curFile.suffix in FILES_TO_SKIP:
        continue

      todos_num, todos = get_todos(abs_path, project_path)
      for t in todos:
        authors.add(t['author'])
      if todos_num != 0:
        retval.append({
          'abs_path': abs_path,
          'num': todos_num,
          'todo_items': todos
        })
  _cache[(_path, project_path)] = retval, list(authors)
  return retval, list(authors)


def get_tree(_path, project_path=None, _cache={}):
  # if (_path, project_path) in _cache:
  #   return _cache[(_path, project_path)]
  if project_path is None:
    project_path = _path
  path = pathlib.Path(_path)
  outputTree = []
  for curFile in path.iterdir():
    # TODO: list of regex to skip.
    if curFile.name.startswith('.') \
      or curFile.name == 'node_modules'\
      or curFile.name == 'public'\
      or curFile.name == 'htmlcov'\
      or curFile.name == '__pycache__':
      continue
    abs_path = str(curFile.resolve())
    item = {
      'abs_path': abs_path,
      'name': curFile.name,
    }
    if curFile.is_dir():
      childs = get_tree(abs_path, project_path)
      childs.sort(key=lambda i: i['name'].lower())
      dirs = list(filter(lambda x: 'children' in x, childs))
      files = list(filter(lambda x: 'children' not in x, childs))
      item['children'] = dirs + files
      item['todos_num'] = sum(i['todos_num'] for i in item['children'])
    else:
      extension = curFile.suffix
      # Could be file name Makefile so the default is txt
      item['file'] = extension[1:] if extension else 'txt'
      if extension not in FILES_TO_SKIP:
        item['todos_num'] = (get_todos(abs_path, project_path, True))[0]
      else:
        item['todos_num'] = 0
    outputTree.append(item)
  outputTree.sort(key=lambda i: i['name'].lower())
  dirs = list(filter(lambda x: 'children' in x, outputTree))
  files = list(filter(lambda x: 'children' not in x, outputTree))
  outputTree = dirs + files
  _cache[(_path, project_path)] = outputTree
  return outputTree


def get_todos(abs_path, project_path, no_git=False):
  todos_count = 0
  todos = []
  line_num = 0
  repo = Repo(project_path)
  try:
    if no_git:
      raise Exception()
    for commit, lines in repo.blame('master', abs_path):
      for line in lines:
        line_num += 1
        if 'TODO:' in line:
          date = datetime.utcfromtimestamp(commit.committed_date).strftime('%Y-%m-%d %H:%M')
          todos.append({
            'date': date,
            'author': commit.author.name,
            'line_num': line_num,
            'text': line
          })
          todos_count += 1
  except Exception:
    with open(abs_path, 'r') as f:
      try:
        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
      except ValueError:
        return todos_count, todos
      for line in iter(m.readline, ''):
        line_num += 1
        if b'' == line:
          break
        if b'TODO:' in line:
          todos.append({
            'date': None,
            'author': None,
            'line_num': line_num,
            'text': line.decode("utf-8")
          })
          todos_count += 1
      m.close()
  return todos_count, todos


def get_stats(project_path,_cache={}):
  # if project_path in _cache:
  #   return _cache[project_path]
  retval = []
  repo = Repo(project_path)
  if repo.bare:
    return None
  for commit in list(repo.iter_commits('master')):
    if 'Vitalii Atamanchuk' not in commit.author.name:
      continue
    date = datetime.utcfromtimestamp(commit.committed_date).strftime('%Y-%m-%d %H:%M:%S')
    item = {
      'date': date,
      'author': commit.author.name,
      'insertions': 0,  # commit.stats.total['insertions']
      'deletions': 0,  # commit.stats.total['deletions']
      'lines': 0,  # commit.stats.total['lines']
    }
    for name, val in commit.stats.files.items():
      if not any([name.endswith(ext) for ext in FILEEXTS_TO_INCLUDE]):
        continue
      if any([re.search(i, name) for i in FILES_REGEX_TO_SKIP_ATGITSTATS]):
        continue
      item['insertions'] += val['insertions']
      item['deletions'] += val['deletions']
      item['lines'] += val['lines']
    retval.append(item)
  _cache[project_path] = retval
  return retval
