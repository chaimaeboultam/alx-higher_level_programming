#!/usr/bin/python3 

for i in range(9):
    for j in range(10):
        print(f"{i}{j}", end='\n' if i == 8 else ", ")

