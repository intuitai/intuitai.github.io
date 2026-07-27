"""Exercise 11.1.3 — a global constant for area

Chapter 11: Scoping — Everyday Programming

Using a global value of pi, this program should compute the area of a
circle with radius 3 and print about 28.27.

This program contains exactly one bug. Solution: sol_11_1_3.py
"""

pi = 3.14159

def circle_area():
    area = pi * 3 * 3

circle_area()
print("Area:", area)
# expected: Area: 28.27431
