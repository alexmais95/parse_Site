import json
from bs4 import BeautifulSoup
from settings import *
import requests


class Open:

    def __init__(self, file=None):
        self.file = file

    def copy_html(self, url):
        reg = requests.get(url)
        src = reg.text
        with open('index_2.html', 'w', encoding='utf-8') as file:
            file.write(src)

    def open_file_html(self, file_r):

        with open(file_r) as file:
            p_g = file.read()

        return p_g

    def open_html_file_insoup(self, page):

        soup = BeautifulSoup(self.open_file_html(page), 'lxml')
        return soup

    def open_html_page_insoup(self, page):

        soup = BeautifulSoup(page.content, 'lxml')
        return soup

    def serch_item(self, search, replase):
        link_dict = {}
        for item in search:
            item_text = item.text
            item_linc = item.get("href")
            for replese in item_text:
                replace_element = replase
                for rep in replace_element:
                    if rep in replese:
                        item_text = item_text.replace(rep, '')
            link_dict[item_text] = item_linc
        return link_dict

    # function that make dictionary: kay=name of link, value=link
    def make_json_file(self, link, replase, count=0):
        src = requests.get(link, headers=headers)
        soup = self.open_html_page_insoup(src)
        text_href = soup.find(class_='mt-3 row m-0 transport-table').find_all('a')
        search = self.serch_item(text_href, replase)

        with open(f'json_file/{count}.json', 'w') as file:
            json.dump(search, file, indent=4, ensure_ascii=False)
