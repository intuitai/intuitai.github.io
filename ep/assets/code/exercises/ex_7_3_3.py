"""Exercise 7.3.3 — Temperature in safe range

Chapter 7: Operators — Everyday Programming

Water is liquid between 0 and 100 degrees Celsius. For 25 degrees this
program should print True.

This program contains exactly one bug. Solution: sol_7_3_3.py
"""

temp_c = 25
in_range = 0 < temp_c > 100
print(in_range)   # expected: True
