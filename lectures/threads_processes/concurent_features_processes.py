import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

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


core_num = multiprocessing.cpu_count()


if __name__ == '__main__':
    with ProcessPoolExecutor(core_num - 2) as executor:
        executor.submit(calculation)
        executor.submit(calculation_1)
        executor.submit(calculation_2)
        executor.submit(calculation)
        executor.submit(calculation_1)
        executor.submit(calculation_2)
