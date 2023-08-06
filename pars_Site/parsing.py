import requests
import lxml
from bs4 import BeautifulSoup
from settings import *
import json


# copy html_page
def copy_html(url, headers):
    reg = requests.get(url, headers=headers)
    src = reg.text
    with open('index.html', 'w') as file:
        file.write(src)


# open copy_html_page
def open_html_page_insoup(page):
    with open(page) as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    return soup


# get from copy_page: href_link, name of link, and save in json_file
def make_json_file(page, name_find_element):
    soup = open_html_page_insoup(page)
    text_href = soup.find_all( class_= name_find_element)

    link_dict = {}
    for item in text_href:
        item_text = item.text.strip('\n')
        item_linc = item.get("href")
        link_dict[item_text] = item_linc

    with open('all_category.json', 'w') as file:
        json.dump(link_dict, file, indent=4, ensure_ascii=False)





