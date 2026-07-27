"""Exercise 16.3.2 — Area of a rectangle

Chapter 16: Handling Failures — Everyday Programming

This program reads two side lengths and, if both parse, prints the area
in the else block.

This program contains exactly one bug. Solution: sol_16_3_2.py
"""

try:
    width = float(input("Width? "))
    height = float(input("Height? "))
except ValueError:
    print("Both sides must be numbers.")
else:
    area = width * height
