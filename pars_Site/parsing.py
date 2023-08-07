import requests
import lxml
from bs4 import BeautifulSoup
from settings import *
import json
import re
import csv


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
def make_json_file(page, replase):
    soup = open_html_page_insoup(page)
    # put your requests in text_href.
    text_href = soup.find()

    link_dict = {}
    for item in text_href:
        item_text = item.text
        item_linc = item.get("href")
        for replese in item_text:
            replace_element = replase
            for rep in replace_element:
                if rep in replese:
                    item_text = item_text.replace(rep, '')
        link_dict[item_text] = item_linc

    with open(f'Link_dict.json', 'w') as file:
        json.dump(link_dict, file, indent=4, ensure_ascii=False)


# make_json_file(copy_page, replase)

# reg = requests.get('https://transport.kr.ua')
# soup = BeautifulSoup(reg.content, 'lxml')
# cards = soup.find(class_='mt-3 row m-0 transport-table').find_all('a')
#
#
# for item in cards:
#     it_text = item.text
#     it_link = item.get('href')
#     print(f'{it_text}:{it_link}')


def search(replase):
    with open('all_category.json') as file:
        page = json.load(file)

    for text, href in page.items():

        src = requests.get(href, headers=headers)
        soup = BeautifulSoup(src.content, 'lxml')

        # put your requests in text_href.
        text_href = soup.find(class_='mt-3 row m-0 transport-table').find_all('a')

        link_dict = {}
        for item in text_href:
            item_text = item.text
            item_linc = item.get("href")
            for replese in item_text:
                replace_element = replase
                for rep in replace_element:
                    if rep in replese:
                        item_text = item_text.replace(rep, '')
            link_dict[item_text] = item_linc
            with open(f'main paig {item_text}.json', 'w') as file:
                json.dump(link_dict, file, indent=4, ensure_ascii=False)

            with open(f'main paig {item_text}.json') as file:
                page = json.load(file)

            for text, href in page.items():

                src = requests.get(href, headers=headers)
                soup = BeautifulSoup(src.content, 'lxml')

                # put your requests in text_href.
                text_href = soup.find(class_='mt-3 row m-0 transport-table').find_all('a')

                link_dict = {}
                for item in text_href:
                    item_text = item.text
                    item_linc = item.get("href")
                    for replese in item_text:
                        replace_element = replase
                        for rep in replace_element:
                            if rep in replese:
                                item_text = item_text.replace(rep, '')
                    link_dict[item_text] = item_linc
            with open(f'all_category{text}.json', 'w') as file:
                json.dump(link_dict, file, indent=4, ensure_ascii=False)

            with open(f'all_category{text}.json') as file:
                page = json.load(file)

# sear = search(replase)
            for text, href in page.items():

                src = requests.get(href, headers=headers)
                soup = BeautifulSoup(src.content, 'lxml')

                # find title
                text_href = soup.find(class_='table').find_all('th')
                str_1 = text_href[0].text
                str_2 = text_href[1].text

                # find time
                time_col = soup.find(class_='table').find_all('td')

                time_b = []
                for item in time_col:
                    td = item.text
                    time_b.append(td)
                time_1 = []
                time_1.append(str_1)
                for item in time_b[0:23:2]:
                    time_1.append(item)

                time_2 = []
                time_2.append(str_2)
                for i in time_b[1:23:2]:
                    time_2.append(i)

                for item in time_1:
                    w = item

                    with open('test_csv.csv', 'a', encoding='utf-8') as file:
                        file_w = csv.writer(file)
                        file_w.writerow(
                            (
                                w

                            )
                        )
                for item in time_2:
                    a = item
                    with open('test_csv.csv', 'a', encoding='utf-8') as file:
                        file_w = csv.writer(file)
                        file_w.writerow(
                            (
                                a

                            )
                        )


search(replase)













