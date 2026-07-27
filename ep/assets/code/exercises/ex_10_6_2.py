"""Exercise 10.6.2 — Unpacking the result

Chapter 10: Functions — Everyday Programming

This program should print the quotient and remainder of 17 divided by 5.

This program contains exactly one bug. Solution: sol_10_6_2.py
"""

def divide(a, b):
    return a // b, a % b

quotient = divide(17, 5)
print(quotient, remainder)  # 3 2
