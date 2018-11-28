from bs4 import BeautifulSoup


class RULES

def get_list_of_used_rags(code):
    soup = BeautifulSoup(code, 'xml')
    used_tags = set()
    for i in soup.find_all():
        print(i.name)
        print(i.attrs)
        if {'v-if', 'v-for'} < set(i.attrs):
            print('error v-if and v-for in the same tag')
        if not ({':key', 'v-for'} < set(i.attrs)):
            print('error tag use v-for without key')

        for prop in i.attrs:
            if not prop.islower():
                print('error prop is not lower')
        print('------'*10)
        used_tags.add(i.name)
    return used_tags
