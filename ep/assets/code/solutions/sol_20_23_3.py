"""Solution 20.23.3 — Checking a measured volume

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

0.1 * 3 does not equal 0.3 exactly in floating-point. Compare with a
tolerance, for example math.isclose.

Exercise: ex_20_23_3.py
"""

import math

pour = 0.1
filled = pour * 3
if math.isclose(filled, 0.3):
    print("Cup is exactly full")
else:
    print("Cup is not exactly full")
