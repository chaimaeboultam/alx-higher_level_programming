#!/usr/bin/python3

def uppercase(s):
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            print("{:c}".format(ord(c) - 32), end='')
        else:
            print("{:c}".format(ord(c)), end='')
