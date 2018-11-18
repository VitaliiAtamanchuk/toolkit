from .api.project import (project_create, project_list, project_delete,
    project_tree, project_stats, get_project_todos)
from .api.path import explore

routers = [
    # TODO: project show all TODOS
    ('POST', '/path/explore', explore),

    ('POST', '/project/add', project_create),
    ('GET', '/project/list', project_list),
    ('DELETE', '/project/delete/{id}', project_delete),
    ('GET', '/project/get/tree/{id}', project_tree),
    ('GET', '/project/get/todos/{id}', get_project_todos),
    ('GET', '/project/get/git/stat/{id}', project_stats),
]
