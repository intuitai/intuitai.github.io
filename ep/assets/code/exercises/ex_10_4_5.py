"""Exercise 10.4.5 — The default is optional

Chapter 10: Functions — Everyday Programming

This program should print 10 by relying on the default increment.

This program contains exactly one bug. Solution: sol_10_4_5.py
"""

def increase(value, by=10):
    return value + by

print(increase())  # 10
