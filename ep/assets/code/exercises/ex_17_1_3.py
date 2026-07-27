"""Exercise 17.1.3 — Average of three grades

Chapter 17: Testing — Everyday Programming

The function should return the average of three test grades, and the
assert should pass for grades 80, 90, and 100.

This program contains exactly one bug. Solution: sol_17_1_3.py
"""

def average(a, b, c):
    return a + b + c / 3

assert average(80, 90, 100) == 90
print("passed")
