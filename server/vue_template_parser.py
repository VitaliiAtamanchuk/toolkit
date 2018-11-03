from bs4 import BeautifulSoup


def get_list_of_used_rags(code):
    soup = BeautifulSoup(code, 'xml')
    used_tags = set()
    for i in soup.find_all():
        used_tags.add(i.name)
    return used_tags
