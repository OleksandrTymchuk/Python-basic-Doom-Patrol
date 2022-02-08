def uppercase(func):
    def inner():
        function = func()
        return function.upper()
    return inner


def split_str(func):
    def inner():
        function = func()
        return function.split()
    return inner


@split_str
@uppercase
def print_text():
    return "Hi there. How are u?"


print(print_text())