"""Solution 16.3.4 — Safe square root

Chapter 16: Handling Failures — Everyday Programming

Bug type: Syntax

The try keyword is missing its colon, so the file will not parse. Add
the colon after try.

Exercise: ex_16_3_4.py
"""

import math

try:
    value = float(input("Enter a number: "))
except ValueError:
    print("That was not a number.")
else:
    print("Square root is", math.sqrt(value))
