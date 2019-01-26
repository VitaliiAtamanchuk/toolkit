from bs4 import BeautifulSoup


# class RULES

def get_list_of_used_rags(code):
    soup = BeautifulSoup(code, 'xml')
    used_tags = set()
    for i in soup.findAll():
        # if {'v-if', 'v-for'} < set(i.attrs):
        #     print('error v-if and v-for in the same tag')
        # if 'v-for' in i.attrs and not ({':key', 'v-for'} < set(i.attrs)):
        #     print('error tag use v-for without key')
        #
        # for prop in i.attrs:
        #     if not prop.islower():
        #         print(f'error prop is not lower {prop}')
        # print('------'*10)
        if i.name in ['template', 'router-view']:
            continue
        used_tags.add(i.name)
    return used_tags
