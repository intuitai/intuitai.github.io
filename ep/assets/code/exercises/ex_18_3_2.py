"""Exercise 18.3.2 — Average of three grades

Chapter 18: Bugs — Everyday Programming

This program should print the average of three test grades.

This program contains exactly one bug. Solution: sol_18_3_2.py
"""

def average(a, b, c):
    return a + b + c / 3

print(average(80, 90, 100))   # expected: 90.0
