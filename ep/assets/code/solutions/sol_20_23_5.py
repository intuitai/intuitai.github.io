"""Solution 20.23.5 — Comparing a savings target

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

1.10 * 3 does not land exactly on 3.30 in floating-point. Compare with a
tolerance using math.isclose.

Exercise: ex_20_23_5.py
"""

import math

weekly = 1.10
saved = weekly * 3
if math.isclose(saved, 3.30):
    print("You reached the target")
else:
    print("You did not reach the target")
