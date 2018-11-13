import pathlib
import json
import mmap
from datetime import datetime

from git import Repo


def get_tree(path):
  path = pathlib.Path(path)
  outputTree = []
  for curFile in path.iterdir():
    if curFile.name.startswith('.') or curFile.name == 'node_modules':
      continue
    item = {
      'name': curFile.name,
    }
    if curFile.is_dir():
      item['children'] = get_tree(curFile)
    else:
      item['file'] = 'txt'
      item['todos_num'] = get_todos(str(curFile.resolve()))
      extension = curFile.suffix
      # Could be file name Makefile so the default is txt
      if extension:
        item['file'] = extension[1:]
    outputTree.append(item)
  return outputTree


def get_todos(abs_path):
  todos_count = 0
  with open(abs_path, 'r') as f:
    try:
      m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    except ValueError:
      return 0
    for line in iter(m.readline, ''):
      if b'' == line:
        break
      if b'TODO:' in line:
        todos_count += 1
        print(f'found in {abs_path} {line}')
    m.close()
  return todos_count


def get_stats(project_path):
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
      'insertions': commit.stats.total['insertions'],
      'deletions': commit.stats.total['deletions'],
      'lines': commit.stats.total['lines'],
    }
    # print(commit.stats.files)
    retval.append(item)
  return retval
