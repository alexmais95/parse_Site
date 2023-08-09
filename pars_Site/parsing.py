import requests
import lxml
from bs4 import BeautifulSoup
from settings import *
import json
import re
import csv
from classmethods import *
import random


# copy html_page
def copy_html(url):
    reg = requests.get(url)
    src = reg.text
    with open('index.html', 'w', encoding='utf-8') as file:
            file.write(src)

page = 'index.html'
json_c = Open()
json_c.make_json_file(page, replase)
def search(replase, file_search):
    with open(file_search) as file:
        page = json.load(file)
    count = 0
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

        with open(f'json_file/{item_text} paig {count}.json', 'w') as file:
            json.dump(link_dict, file, indent=4, ensure_ascii=False)

        with open(f'json_file/{item_text} paig {count}.json') as file:
            page = json.load(file)

        for text, href in page.items():

            src = requests.get(href, headers=headers)
            soup = BeautifulSoup(src.content, 'lxml')

            # find title
            text_href = soup.find(class_='table').find_all('th')
            
            try:
                str_1 = text_href[0].text


            except IndexError:
                continue
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
            time_2.append(str_1)
            for i in time_b[1:23:2]:
                time_2.append(i)

            for item in time_1:
                w = item

                with open(f'csv_file/{item_text} {count}.csv', 'a', encoding='utf-8') as file:
                    file_w = csv.writer(file)
                    file_w.writerow(
                        (
                            w

                        )
                    )
            for item in time_2:
                a = item
                with open(f'/csv_file{item_text} {count}.csv', 'a', encoding='utf-8') as file:
                    file_w = csv.writer(file)
                    file_w.writerow(
                        (
                            a

                        )
                    )
        count+=1

#search(replase, file_search)