import time
from datetime import datetime


def logger(logfile):
    def logging_decorator(func):
        def inner(*args, **kwargs):
            log = f'{func.__name__} with was executed at {datetime.now()}\n'
            print(log)
            with open(logfile, 'a') as file:
                file.write(log + '\n')
        return inner
    return logging_decorator


@logger(logfile='out.log')
def my_func():
    """
    This is my func
    """
    print(f'{my_func().__name__} is running')


my_func()
