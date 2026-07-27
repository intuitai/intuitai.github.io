"""Exercise 13.1.1 — Square root with math

Chapter 13: Modules — Everyday Programming

This program should print the length of the hypotenuse of a right
triangle with legs 3 and 4 (it should be 5.0).

This program contains exactly one bug. Solution: sol_13_1_1.py
"""

import math

leg_a = 3
leg_b = 4
hypotenuse = math.sqrt(leg_a ** 2 - leg_b ** 2)
print(hypotenuse)   # 5.0
