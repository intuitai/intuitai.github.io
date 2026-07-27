"""Exercise 13.2.2 — Calling with the module prefix

Chapter 13: Modules — Everyday Programming

This two-file program should print the area of a 4-by-6 rectangle (24).

This program contains exactly one bug. Solution: sol_13_2_2.py
"""

# file: geometry.py
def rectangle_area(width, height):
    return width * height

# file: main.py
import geometry

print(rectangle_area(4, 6))   # 24
