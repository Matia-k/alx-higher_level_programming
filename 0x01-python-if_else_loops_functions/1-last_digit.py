#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string_number = str(number)
if string_number[0] == '-':
    sign = -1
else:
    sign == 1

len_number = len(string_number)
digit = int(string_number[len_number - 1]) * sign

if digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")
else:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
