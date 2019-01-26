import csv
import urllib.request

from bs4 import BeautifulSoup


def fetch_and_save_html5_tags_list():
    url = 'https://www.w3schools.com/tags/'
    f = urllib.request.urlopen(url)
    html_code = f.read().decode('utf-8')

    soup = BeautifulSoup(html_code, 'html.parser')

    tags_list = []
    for tag in soup.select('tr td a'):
        tags_list.append(tag.getText())

    with open('app/core/html_tags.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(tags_list)
    return tags_list


def get_html5_tags_set():
    tags_set = set()
    with open('app/core/html_tags.csv', 'r', newline='') as myfile:
        rows = csv.reader(myfile, quoting=csv.QUOTE_ALL)
        for row in rows:
            tags_set.update(row)
    return tags_set
