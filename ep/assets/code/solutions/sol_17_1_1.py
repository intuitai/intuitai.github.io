"""Solution 17.1.1 — Rectangle area check

Chapter 17: Testing — Everyday Programming

Bug type: Logical

The function adds length and width instead of multiplying them, so it
returns 7 and the assert fails. Area of a rectangle is length times
width.

Exercise: ex_17_1_1.py
"""

def rectangle_area(length, width):
    return length * width

assert rectangle_area(4, 3) == 12
print("passed")
