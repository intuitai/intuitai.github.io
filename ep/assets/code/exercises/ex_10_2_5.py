"""Exercise 10.2.5 — Two parameters

Chapter 10: Functions — Everyday Programming

This program should compute the perimeter of a rectangle (2 times width
plus 2 times height) for a 3 by 5 rectangle, giving 16.

This program contains exactly one bug. Solution: sol_10_2_5.py
"""

def perimeter(width, height):
    return 2 * width + 2 * width

print(perimeter(3, 5))  # 16
