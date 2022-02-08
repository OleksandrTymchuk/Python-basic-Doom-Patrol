def my_decorator(func):
    def inner():
        print('Print before function')
        func()
        print('Print after function')

    return inner


@my_decorator
def foo():
    print('Hi there')


# foo = my_decorator(foo)
foo()

