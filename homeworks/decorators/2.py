import time


class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f'{self.func.__name__} rintime is {end - start}')
        return result


@Timer
def some_function(delay):
    # Introducing some time delay to
    # simulate a time taking function.
    time.sleep(delay)


some_function(3)
