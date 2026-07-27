"""Solution 10.2.3 — Too many arguments

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The function takes two parameters but the call passes three, raising a
TypeError. Pass exactly width and height.

Exercise: ex_10_2_3.py
"""

def rectangle_area(width, height):
    return width * height

print(rectangle_area(4, 6))
