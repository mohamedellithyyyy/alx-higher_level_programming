#!/usr/bin/python3

import random

# Assigning a random signed number to the variable 'number' each time the program is executed
number = random.randint(-10, 10)

# Printing whether the number is positive, negative, or zero
print(number)
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
