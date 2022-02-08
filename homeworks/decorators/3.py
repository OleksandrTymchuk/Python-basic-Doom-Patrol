class WrongFactorialNumber(Exception):
    def __init__(self, num, message=' - wrong number to calculate factorial'):
        self.num = num
        self.message = message

    def __str__(self):
        return f'{self.num} {self.message}'


def number_verification(func):
    def inner(num):
        if isinstance(num, int) and num > 0:
            return func(num)
        else:
            print(f' ur number: {num}, U have to use only positive and integer nums')

    return inner


@number_verification
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(-10))
