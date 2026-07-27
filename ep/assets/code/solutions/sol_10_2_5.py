"""Solution 10.2.5 — Two parameters

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The formula uses width twice, ignoring the second parameter. It should
be 2 * width + 2 * height to use both arguments.

Exercise: ex_10_2_5.py
"""

def perimeter(width, height):
    return 2 * width + 2 * height

print(perimeter(3, 5))  # 16
