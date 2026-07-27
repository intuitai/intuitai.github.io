"""Exercise 13.1.5 — Rounding a price up

Chapter 13: Modules — Everyday Programming

This program should round a price of $4.20 up to the next whole dollar
using a from-import.

This program contains exactly one bug. Solution: sol_13_1_5.py
"""

from math import ceil

price = 4.20
rounded_up = math.ceil(price)
print(rounded_up)   # 5
