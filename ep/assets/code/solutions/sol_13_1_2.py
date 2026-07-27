"""Solution 13.1.2 — Circle area with pi

Chapter 13: Modules — Everyday Programming

Bug type: Runtime

math.pi is a value (a float), not a function, so calling it as math.pi()
raises TypeError: 'float' object is not callable. Remove the parentheses
and multiply by the value directly.

Exercise: ex_13_1_2.py
"""

import math

radius = 5
area = math.pi * radius ** 2
print(area)   # about 78.54
