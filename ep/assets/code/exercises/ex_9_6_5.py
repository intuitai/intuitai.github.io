"""Exercise 9.6.5 — Sum until limit

Chapter 9: Control Flow — Everyday Programming

This program should add 1, 2, 3, ... until the total reaches at least
10, then print the total, 10.

This program contains exactly one bug. Solution: sol_9_6_5.py
"""

total = 0
number = 1

while total < 10:
    number += 1
    total += number

print(total)
# Expected: 10
