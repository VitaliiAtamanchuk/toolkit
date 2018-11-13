from .api.project import get_stat

routers = [
    ('POST', '/project/add', get_stat),
    ('GET', '/project/list', get_stat),
    ('DELETE', '/project/list', get_stat),
    ('GET', '/project/get/{id}/tree', get_stat),
    ('GET', '/project/get/{id}/git/stat', get_stat),
]
