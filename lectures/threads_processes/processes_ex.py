import time
from multiprocessing import Process


def print_user_input():
    start = time.time()
    user_input = 'tests'
    print(f'Hello, your text: {user_input}')
    print(f'print_user_input time: {time.time() - start}')


def calculation():
    print('Starting calculation 1')
    start = time.time()
    a = [x ** 3 for x in range(1500000)]
    print(f'calculation time: {time.time() - start}')


def calculation_1():
    print('Starting calculation 2')
    start = time.time()
    a = [x ** 3 for x in range(1500000)]
    print(f'calculation time: {time.time() - start}')


def calculation_2():
    print('Starting calculation 3')
    start = time.time()
    a = [x ** 3 for x in range(1500000)]
    print(f'calculation time: {time.time() - start}')


start = time.time()
calculation()
calculation_1()
calculation_2()
print(f'Single process total time: {time.time() - start}')

process_1 = Process(target=calculation)
process_2 = Process(target=calculation_1)
process_3 = Process(target=calculation_2)
process_1.start()
process_2.start()
process_3.start()

start_1 = time.time()
process_1.join()
process_2.join()
process_3.join()
print(f'Three processes total time: {time.time() - start_1}')


