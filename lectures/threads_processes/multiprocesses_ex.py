import time
from multiprocessing import Process
import os


def foo():
    print('calling foo')
    print(f'parent processes id: {os.getppid()}')
    print(f'process id: {os.getpid()}')
    time.sleep(2)


def main():
    print('calling main')
    p = Process(name='Service1', target=foo)
    p.start()
    p.join()
    print(f'Process p is alive: {p.is_alive()}')
    p.join()


if __name__ == '__main__':
    main()
