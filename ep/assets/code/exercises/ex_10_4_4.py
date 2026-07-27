"""Exercise 10.4.4 — Order of defaults

Chapter 10: Functions — Everyday Programming

This function gives the area of a rectangle, using a default height of
1.

This program contains exactly one bug. Solution: sol_10_4_4.py
"""

def area(height=1, width):
    return width * height

print(area(width=5))  # 5
