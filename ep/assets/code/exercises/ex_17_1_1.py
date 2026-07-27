"""Exercise 17.1.1 — Rectangle area check

Chapter 17: Testing — Everyday Programming

The function should return the area of a rectangle, and the assert
should pass for a 4 × 3 rectangle.

This program contains exactly one bug. Solution: sol_17_1_1.py
"""

def rectangle_area(length, width):
    return length + width

assert rectangle_area(4, 3) == 12
print("passed")
