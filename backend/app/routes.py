from .api.project import (project_create, project_list, project_delete,
    project_tree, project_stats, get_project_todos)
from .api.path import explore
from .api.code_analysis import py_isort_diff, get_vue_file_hierarchy, py_isort_fix, py_mccabe, get_file_todos

routers = [
    ('POST', '/path/explore', explore),

    ('POST', '/code-analysis/py-isort-diff', py_isort_diff),
    ('POST', '/code-analysis/py-isort-fix', py_isort_fix),
    ('POST', '/code-analysis/py-mccabe', py_mccabe),
    ('POST', '/code-analysis/get-file-todos', get_file_todos),
    ('POST', '/code-analysis/get-vue-file-hierarchy', get_vue_file_hierarchy),

    ('POST', '/project/add', project_create),
    ('GET', '/project/list', project_list),
    ('DELETE', '/project/delete/{id}', project_delete),
    ('GET', '/project/get/tree/{id}', project_tree),
    ('GET', '/project/get/todos/{id}', get_project_todos),
    ('GET', '/project/get/git/stat/{id}', project_stats),
]
