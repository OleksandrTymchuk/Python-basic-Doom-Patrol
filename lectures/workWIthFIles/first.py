with open('files/file.txt', 'r') as file:
    print(file.read())
    file.write('\n Lol')
    print(file.read())