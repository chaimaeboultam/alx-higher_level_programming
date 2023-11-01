#!/usr/bin/python3

def islower(c):
    return ord('a') <= ord(c) <= ord('z')

def uppercase(s):
    for c in s:
        print("{:c}".format(ord(c) if not islower(c) else ord(c) - 32), end="")
    print("")
