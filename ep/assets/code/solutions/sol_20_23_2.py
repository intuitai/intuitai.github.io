"""Solution 20.23.2 — Adding two distances

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

0.1 + 0.2 is slightly more than 0.3 in floating-point, so the exact
comparison is False. Use math.isclose to compare with tolerance.

Exercise: ex_20_23_2.py
"""

import math

leg_one = 0.1
leg_two = 0.2
if math.isclose(leg_one + leg_two, 0.3):
    print("Distances match")
else:
    print("Distances do not match")
