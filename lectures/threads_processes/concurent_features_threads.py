from threading import Thread
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen


def print_user_input():
    start = time.time()
    user_input = input('Enter smth: ')
    print(f'Hello, ur text: {user_input}')
    print(f'print_user_input: {time.time()- start}')


def calculation(b):
    print('Starting calculation')
    start = time.time()
    a = [x ** 3 for x in range(1500000)]
    print(f'calculation time {time.time() - start}')


# with ThreadPoolExecutor(max_workers=5) as pool:
#     pool.submit(calculation)
#     pool.submit(print_user_input)


urls = ['https://google.com', 'http://www.python.org', 'http://facebook.com']

with ThreadPoolExecutor(4) as executor:
    results = executor.map(urlopen, urls)
    print(list(results))

