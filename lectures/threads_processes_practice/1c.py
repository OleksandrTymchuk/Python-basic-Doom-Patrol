"""
1. Create a script that download content over the network. The script should be able to
download web pages from a few sites, but it really could be any network traffic.
1c. With multiprocessing
"""

import requests
import time
import psutil
from concurrent.futures import ProcessPoolExecutor

session = None
core_num = psutil.cpu_count()
urls = ['https://google.com/',
        'https://uk.wikipedia.org/',
        'https://refactoring.guru/uk',
        'https://www.python.org/',
        'https://cursor.education/uk/'] * 50


def get_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        print(f'Reading {len(response.content)} for {url}')


def download_all_sites(urls):
    with ProcessPoolExecutor(core_num - 1) as executor:
        executor.map(download_site, urls)


if __name__ == '__main__':
    start = time.time()
    get_session()
    download_all_sites(urls)
    print(f'Total Time for getting the content of {len(urls)} sites: {time.time() - start}')

