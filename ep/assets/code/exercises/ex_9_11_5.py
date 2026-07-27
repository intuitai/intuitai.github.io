"""Exercise 9.11.5 — Absolute value

Chapter 9: Control Flow — Everyday Programming

This function should return the absolute value of a number. absolute(7)
should print 7.

This program contains exactly one bug. Solution: sol_9_11_5.py
"""

def absolute(number):
    if number < 0:
        return -number

print(absolute(7))
# Expected: 7
