"""Solution 13.1.3 — Rolling a die

Chapter 13: Modules — Everyday Programming

Bug type: Logical

random.randint(a, b) includes *both* endpoints, so randint(1, 7) can
return 7, which is impossible on a six-sided die. Use random.randint(1,
6).

Exercise: ex_13_1_3.py
"""

import random

roll = random.randint(1, 6)
print(roll)   # a number from 1 to 6
