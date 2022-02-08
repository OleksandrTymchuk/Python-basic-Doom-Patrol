import sys

# print(f'This is the name of this program: {sys.argv[0]}')
# print(f'Number of elements including the name of the program: {len(sys.argv)}')
# print(f'Number of elements without name of the program: {len(sys.argv) - 1}')
# print(str(sys.argv))
# username = sys.argv[1]
# email = sys.argv[2]
# num_of_elem = len(sys.argv) - 1
# for e in range(1, num_of_elem + 1):
#     print(sys.argv[e])

try:
    name = sys.argv[1]
    username = sys.argv[2]
    email = sys.argv[3]
    print(name, username, email)
except IndexError:
    raise Exception('This script should apply the next args: {name} {username} {email}')


