import sys
import getopt

args = sys.argv[1:]
print(args)
username = None
email = None
opts = []

try:
    opts, args = getopt.getopt(args, "u:e:",
                               ["username=",
                                "email="])
except Exception as e:
    print(f'Error: {e}')

for opt, arg in opts:
    if opt in ['-u', '--username']:
        username = arg
    elif opt in ['-e', '--email']:
        email = arg

print(username, email)
