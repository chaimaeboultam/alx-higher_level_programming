#!/usr/bin/python3

for i in range(ord('a'), ord('z') + 1):
    if ord(i) != 'e' and ord(i) != 'q':
        print("{:c}".format(i), end="")
