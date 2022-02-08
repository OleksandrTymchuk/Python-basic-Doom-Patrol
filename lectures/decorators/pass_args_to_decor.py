def tag(tag_name):
    def inner(func):
        def wrapper(*args):
            return f'<{tag_name}>{func(args)}</{tag_name}>'

        return wrapper

    return inner


@tag('b')
def get_text(name):
    return f'Hello {name}'


print(get_text('Alex'))
