def from_lst_to_str(func):
    def inner(n):
        result = func(n)
        str_res = ''.join([str(item) for item in result])
        return str_res
    return inner


@from_lst_to_str
def sequence(sequence_len):
    lst = []
    for i in range(1, sequence_len + 1):
        x = 0
        while i != x:
            lst.append(i)
            x += 1
    return lst[:sequence_len]


print(sequence(7))
