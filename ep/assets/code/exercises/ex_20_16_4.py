"""Exercise 20.16.4 — Perimeter of a rectangle

Chapter 20: Common Pitfalls — Everyday Programming

The program should print the perimeter of a 6 by 4 rectangle.

This program contains exactly one bug. Solution: sol_20_16_4.py
"""

def perimeter(length, width):
    p = 2 * (length + width)

print("Perimeter:", perimeter(6, 4))
