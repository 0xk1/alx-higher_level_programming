#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10 if number > 0 else number % -10
msg = "greater than 5" if last > 5 else last if last == 0 \
       else "less than 6 and not 0"
print(f"Last digit of {number} is {last} and is {msg}")
