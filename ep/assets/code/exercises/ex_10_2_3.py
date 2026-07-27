"""Exercise 10.2.3 — Too many arguments

Chapter 10: Functions — Everyday Programming

This program should print the area of a rectangle that is 4 by 6.

This program contains exactly one bug. Solution: sol_10_2_3.py
"""

def rectangle_area(width, height):
    return width * height

print(rectangle_area(4, 6, 8))
