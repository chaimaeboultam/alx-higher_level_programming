#!/usr/bin/python3

def islower(c):
    for i in range(ord'a',ord'z'+1):
        if c not in i:
            return False
        else:
            return True
