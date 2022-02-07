from bs4 import BeautifulSoup
import csv
from config import Config
import requests


def create_file():
    file = open(Config.FILE_URL, 'w')
    csvwriter = csv.writer(file)
    csvwriter.writerow(['title', 'price', 'description'])
    file.close()


def get_count_of_pages(content):
    soup = BeautifulSoup(content, 'html.parser')
    pagination_list = soup.find(class_='pagination')
    last_el = pagination_list.find_all('li')[-1].find('a')
    link = last_el['href']
    return link[-1]


def save_row(data):
    file = open(Config.FILE_URL, 'a')
    writer = csv.writer(file)
    writer.writerows(data)
    file.close()


def get_description(content):
    soup = BeautifulSoup(content, 'html.parser')
    all_items = soup.find_all(class_='description')
    for item in all_items:
        description_object = item.find(class_='description__text js-hidden-content')
        true_description = description_object.find('p').text
        return true_description


def get_all_items(content):
    soup = BeautifulSoup(content, 'html.parser')
    items_list = []
    all_items = soup.find_all(class_='catalog-item__entry')
    for item in all_items:
        title_object = item.find(class_='catalog-item__title')
        title = title_object.find('a').text
        price = item.find(class_='catalog-item__price').text
        href = requests.get(title_object.find('a').get('href'))
        true_description = href.content
        description = get_description(true_description)

        items_list.append([title, price, description])
    save_row(items_list)
