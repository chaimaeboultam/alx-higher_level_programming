#!/usr/bin/python3

for i in range(ord('A'), ord('Z') + 1):
    if chr(i) != 'E' and chr(i) != 'Q':
        print("{:c}".format(i), end="")
