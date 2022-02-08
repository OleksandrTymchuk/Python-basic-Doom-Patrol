# input as ﬂat text
a = 'test'
# the same input can also be read from a ﬁle
# returns a printable representation of the input;
# the output can be written to a ﬁle as well
print(repr(a))
# write content to ﬁles using repr
with open('test.txt', 'a') as f:
    f.write(repr(a))
