"""Exercise 20.15.4 — Area of a circle

Chapter 20: Common Pitfalls — Everyday Programming

This program should compute and print the area of a circle with radius
4.

This program contains exactly one bug. Solution: sol_20_15_4.py
"""

import math

def circle_area(radius):
    return math.pi * radius ** 2

print("Area:", circle_area(4))
print("Half area:", circle_area / 2)
