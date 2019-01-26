from pathlib import Path

from fetch_html5_tags import get_html5_tags_set
from vue_template_parser import get_list_of_used_rags


if __name__ == '__main__':

    code = Path('code.vue').read_text()
    import re
    rex = re.compile(r'<template lang="html">.*?</template>',re.MULTILINE|re.DOTALL)
    match = rex.match(code)
    text = match.group()
    # html5_tags = get_html5_tags_set()
    # used_tags = get_list_of_used_rags(code)
    # print(used_tags)
    # from bs4 import BeautifulSoup
#     x="""<foo>
#    <bar>
#       <type asd foobar="1"/>
#       <type foobar="2"/>
#    </bar>
# </foo>"""
#     x = """<v-flex xs7 class='px-2 mt-2'>
#   <TheMain asdSds='as' sd class='sd' />
# </v-flex>"""
#     y=BeautifulSoup(x)
#     for i in y.findAll():
#         print(dir(i))
#         print(i.name)
#         print(i.namespace)
#         print(i.attrs)
#         print(i.tag_name_re)
