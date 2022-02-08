import argparse

parser = argparse.ArgumentParser(description='Lecture parser')
parser.add_argument('-s', '--status', dest='st')

args = parser.parse_args()

a = args.st
print(a)
