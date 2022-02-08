import requests
from config import Config
from parsing import get_count_of_pages


response = requests.get(Config.PARSING_URL)
count_of_pages = get_count_of_pages(response.content)

for i in range(1, int(count_of_pages) + 1):
    print(Config.PARSING_URL + '?page=' + str(i))

