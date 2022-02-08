# import argparse
#
# parser = argparse.ArgumentParser(description='Lecture parser')
# parser.add_argument('-s', '--status', default='Done', type=str, required=True, dest='st',
#                     help='This is a variable for status', nargs=5)
#
# args = parser.parse_args()
#
# status = args.st
# print(status)

import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("-a", default=1, type=int, help="This is the 'a' variable")
parser.add_argument("-education",
                    choices=["highschool", "college", "university", "other"],
                    required=True, type=str, help="Your name")
args = parser.parse_args()
ed = args.education
if ed == "college" or ed == "university":
    print("Has degree")
elif ed == "highschool":
    print("Finished Highschool")
else:
    print("Does not have degree")


# import argparse
#
# parser = argparse.ArgumentParser(description='A tutorial of argparse!')
# parser.add_argument("-a", action="store_true", help="This is the 'a' variable")
# parser.add_argument("-b", action="append", help="This is the 'b' variable")
# parser.add_argument("-c", action='version', help="This is the 'b' variable")
# args = parser.parse_args()
# a = args.a
# b = args.b
# c = args.c
# print(a)
# print(b)
# print(c)