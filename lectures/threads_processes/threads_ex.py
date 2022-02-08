from threading import Thread
import time


def print_user_input():
    start = time.time()
    user_input = input('Enter smth: ')
    print(f'Hello, ur text: {user_input}')
    print(f'print_user_input: {time.time()- start}')


def calculation():
    print('Starting caltucalion')
    start = time.time()
    a = [x ** 3 for x in range(1500000)]
    print(f'calculation time {time.time() - start}')


start = time.time()
print_user_input()
calculation()
print(f'Single thread total time {time.time() - start}')

thread_1 = Thread(target=calculation())
thread_2 = Thread(target=print_user_input())

start1 = time.time()

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
print(f'Two threads total time: {time.time() - start1}')
