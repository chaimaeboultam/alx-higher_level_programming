#!/usr/bin/python3

for i in range(ord('A'), ord('Z') + 1):
    if i != 'E' and i != 'Q':
        print("{:c}".format(i), end="")
