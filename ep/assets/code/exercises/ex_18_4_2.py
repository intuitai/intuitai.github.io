"""Exercise 18.4.2 — Circle circumference

Chapter 18: Bugs — Everyday Programming

This program should print the circumference of a circle with radius 5,
but the answer is wrong. Trace it with print and find the single wrong
line.

This program contains exactly one bug. Solution: sol_18_4_2.py
"""

def circumference(radius):
    pi = 3.14159
    return pi * radius

print(circumference(5))   # expected: about 31.4
