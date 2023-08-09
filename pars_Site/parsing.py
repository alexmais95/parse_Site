import requests
import lxml
from bs4 import BeautifulSoup
from settings import *
import json
import re
import csv
from classmethods import *
import random
import os


def search(replase, file_search):
    with open(file_search) as file:
        page = json.load(file)
    count = 0
    json_c = Open()
    for text, href in page.items():

        json_c.make_json_file(href, replase, count)

        with open(f'json_file/{count}.json') as file:
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

                with open(f'csv_file/{count}.csv', 'a', encoding='utf-8') as file:
                    file_w = csv.writer(file)
                    file_w.writerow(
                        (
                            w

                        )
                    )
            for item in time_2:
                a = item
                with open(f'csv_file/{count}.csv', 'a', encoding='utf-8') as file:
                    file_w = csv.writer(file)
                    file_w.writerow(
                        (
                            a

                        )
                    )
        count+=1


if __name__ == '__main__':
    search(replase, file_search)