"""Exercise 18.4.3 — Sum of a list

Chapter 18: Bugs — Everyday Programming

This program should print the sum of the daily rainfall totals, but the
answer is wrong. Trace it with print and find the single wrong line.

This program contains exactly one bug. Solution: sol_18_4_3.py
"""

rainfall = [1.2, 0.8, 2.0, 1.5]
total = 0
for amount in rainfall:
    total = amount
print(total)   # expected: 5.5
