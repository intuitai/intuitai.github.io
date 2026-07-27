"""Exercise 7.3.5 — Within speed limit

Chapter 7: Operators — Everyday Programming

The speed limit is 65. For a speed of 65 this program should report that
the driver is within the limit and print True.

This program contains exactly one bug. Solution: sol_7_3_5.py
"""

speed = 65
limit = 65
within_limit = speed < limit
print(within_limit)   # expected: True
