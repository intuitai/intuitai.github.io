"""Exercise 10.9.4 — Unpacking into a call

Chapter 10: Functions — Everyday Programming

This program should pass the list as separate positional arguments and
print 6.

This program contains exactly one bug. Solution: sol_10_9_4.py
"""

def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add_three(numbers))  # 6
