from bs4 import BeautifulSoup
import re


def get_count_of_pages(content):
    soup = BeautifulSoup(content, 'html.parser')
    pagination_list = soup.find(class_='pagination')
    last_el = pagination_list.find_all('li')[-1].find('a')
    link = last_el['href']
    print(link[-1])



