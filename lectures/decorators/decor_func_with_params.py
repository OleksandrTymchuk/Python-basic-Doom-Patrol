# def smart_divide(func):
#     def inner(a, b):
#         print(f'Im going to divide {a} on {b}')
#         if b == 0:
#             print('Whoops, Im not able to divide by 0')
#             return 0
#         else:
#             result = func(a, b)
#             return result
#
#     return inner

def smart_divide(func):
    def inner(*args, **kwargs):
        a = args[0]
        b = args[1]
        c = kwargs['test']
        print(c)
        print(f'Im going to divide {a} on {b}')
        if b == 0:
            print('Whoops, Im not able to divide by 0')
            return False
        else:
            result = func(a, b)
            return result

    return inner

@smart_divide
def divide(a, b, c):
    return a / b


print(divide(1, 0, test='test'))