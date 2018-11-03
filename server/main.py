from pathlib import Path

from fetch_html5_tags import get_html5_tags_set
from vue_template_parser import get_list_of_used_rags


if __name__ == '__main__':
    code = Path('code.vue').read_text()

    html5_tags = get_html5_tags_set()
    used_tags = get_list_of_used_rags(code)
