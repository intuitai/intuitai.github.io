"""Exercise 10.6.1 — Returning a pair

Chapter 10: Functions — Everyday Programming

This program should print the smallest and largest of three
temperatures.

This program contains exactly one bug. Solution: sol_10_6_1.py
"""

def min_max(a, b, c):
    return min(a, b, c)

low, high = min_max(31.0, 36.5, 33.0)
print(low, high)  # 31.0 36.5
