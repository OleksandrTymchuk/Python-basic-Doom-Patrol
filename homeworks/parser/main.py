import requests
from config import Config
from parsing import get_count_of_pages, get_all_items, create_file


response = requests.get(Config.PARSING_URL)
count_of_pages = get_count_of_pages(response.content)


create_file()

for page_number in range(1, int(count_of_pages) + 1):
    page_link = Config.PARSING_URL + '?page=' + str(page_number)
    response = requests.get(page_link)
    get_all_items(response.content)
