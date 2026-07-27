"""Exercise 5.3.5 — Within speed limit

Chapter 5: Data Structures — Everyday Programming

The limit is 65. A car going 60 is within the limit, so the program
should print True.

This program contains exactly one bug. Solution: sol_5_3_5.py
"""

speed = 60
limit = 65

within_limit = speed > limit
print(within_limit)   # True
