"""Solution 20.15.4 — Area of a circle

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

circle_area / 2 tries to divide the function object by 2, raising
TypeError. Call the function first, then divide its result.

Exercise: ex_20_15_4.py
"""

import math

def circle_area(radius):
    return math.pi * radius ** 2

print("Area:", circle_area(4))
print("Half area:", circle_area(4) / 2)
