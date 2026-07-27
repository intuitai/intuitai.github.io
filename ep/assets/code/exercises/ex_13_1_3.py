"""Exercise 13.1.3 — Rolling a die

Chapter 13: Modules — Everyday Programming

This program should print a random whole number from 1 to 6, like
rolling a single die.

This program contains exactly one bug. Solution: sol_13_1_3.py
"""

import random

roll = random.randint(1, 7)
print(roll)   # a number from 1 to 6
