"""Exercise 16.3.4 — Safe square root

Chapter 16: Handling Failures — Everyday Programming

This program reads a number and, only if it parses, prints its square
root in the else block.

This program contains exactly one bug. Solution: sol_16_3_4.py
"""

import math

try
    value = float(input("Enter a number: "))
except ValueError:
    print("That was not a number.")
else:
    print("Square root is", math.sqrt(value))
