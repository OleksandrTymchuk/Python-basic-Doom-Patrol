# 1

def double_result(func):
    def inner(a, b):
        return (a + b) * 2
    return inner


def add(a, b):
    return a + b


@double_result
def add(a, b):
    return a + b


print(add(5, 5))

# 2


def only_odd_parameters(func1):
    def inner(*args):
        for i in args:
            if i % 2 == 0:
                return "Please use only odd numbers!"
        return func1(*args)
    return inner


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))
print(add(4, 4))


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(multiply(5, 5, 5, 5, 5))
print(multiply(4, 4, 4, 4, 4))

# 3


def logged(func):
    def inner(*args):
        return f"you called {func.__name__}{args} \n" \
               f"it returned {func(*args)}"
    return inner


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))

# 4


def type_check(correct_type):
    def inner(func):
        def wrapper(*args):
            if isinstance(args[0], correct_type):
                return func(args[0])
            else:
                return f'Wrong Type: {type(args[0])}'
        return wrapper
    return inner


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
