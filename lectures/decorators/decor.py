def func(x):
    return x


def func1():
    print('Hello')


func(func1())


def foo(bar):
    return bar + 1

print(foo)
print(foo(2))
print(type(foo))