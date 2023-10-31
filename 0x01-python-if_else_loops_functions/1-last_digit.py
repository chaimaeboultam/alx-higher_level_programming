#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
rest = number % 10 if number >10 else number % -10

if number > 5:
    print(f"Last digit of {number} is {rest} and is greater than 5")
elif number < 6 and number != 0:
    print(f"Last digit of {number} is {rest} and is less than 6 and not 0")
elif number == 0:
    print(f"Last digit of {number} is {rest} and is 0")
else:
    pass
