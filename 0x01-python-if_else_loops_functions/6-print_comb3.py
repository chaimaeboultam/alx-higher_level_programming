#!/usr/bin/python3 

for i in range(9):
    for j in range(10):
        if i<j:
            print("{:d}{:d}".format(i,j), end='\n' if i == 8 and i==9 else ", ")

