"""
1. Create a script that download content over the network. The script should be able to
download web pages from a few sites, but it really could be any network traffic.
1b. With multithreading
"""

import requests
import time
from concurrent.futures import ThreadPoolExecutor
import threading
import psutil

core_num = psutil.cpu_count()
print(core_num)

urls = ['https://google.com/',
        'https://uk.wikipedia.org/',
        'https://refactoring.guru/uk',
        'https://python.org/',
        'https://cursor.education/uk/'] * 50

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f'Reading {len(response.content)} for {url}')


def download_all_sites(urls):
    with ThreadPoolExecutor(core_num - 1) as executor:
        executor.map(download_site, urls)


if __name__ == '__main__':
    start = time.time()
    download_all_sites(urls)
    print(f'Total time for getting the content of {len(urls)} sites: {time.time() - start}')
