"""Solution 20.16.4 — Perimeter of a rectangle

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The perimeter p is calculated but never returned, so the program prints
None. Return p.

Exercise: ex_20_16_4.py
"""

def perimeter(length, width):
    p = 2 * (length + width)
    return p

print("Perimeter:", perimeter(6, 4))
