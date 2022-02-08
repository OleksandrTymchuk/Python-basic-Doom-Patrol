import time


def timer(func):
    def inner():
        start = time.time()
        func()
        result = time.time() - start
        return result

    return inner


@timer
def calculate():
    for i in range(100000000):
        pass


print(calculate())


