"""Solution 20.23.1 — Splitting a bill exactly

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

0.10 + 0.10 + 0.10 is not exactly 0.30 in binary floating-point, so the
equality fails. Compare with a small tolerance using round or
math.isclose.

Exercise: ex_20_23_1.py
"""

import math

share = 0.10
total = share + share + share
if math.isclose(total, 0.30):
    print("The shares add up exactly")
else:
    print("The shares do not add up exactly")
