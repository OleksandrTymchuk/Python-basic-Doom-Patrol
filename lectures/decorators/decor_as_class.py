class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('Before func()')
        self.func()
        print('After func()')


@MyDecorator
def foo():
    print('Test')


foo()