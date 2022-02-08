def parent():
    print('Print from the parent() function')
    foo = 'Hello'

    def first_child():
        print(f'Print from the first_child() function: {foo}')

    def second_child():
        print(f'Print from the second_child() function: {foo}')

    first_child()
    second_child()


def calculate_smth(a, b):
    c = a + b * (b + a)

    def pow_it(c):
        return c**2

    c = pow_it(c)
    print(c)


calculate_smth(5, 7)


parent()