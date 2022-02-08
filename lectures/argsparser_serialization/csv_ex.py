# Reading CSV content from a ﬁle
import csv

# with open('addresses.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
iterable = []
with open('addresses.csv', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(iterable)
