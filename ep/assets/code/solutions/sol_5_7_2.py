"""Solution 5.7.2 — A fixed pair

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

Tuples are immutable, so size[0] = 1280 raises a TypeError. You cannot
change one element in place; build a new tuple instead.

Exercise: ex_5_7_2.py
"""

size = (1920, 1080)
size = (1280, size[1])
print(size)   # (1280, 1080)
