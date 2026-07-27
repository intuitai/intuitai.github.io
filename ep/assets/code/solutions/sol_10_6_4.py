"""Solution 10.6.4 — Order of the tuple

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The tuple is returned as (3, 8) but the caller expects width first, so
width prints as 3. Return width then height: return 8, 3.

Exercise: ex_10_6_4.py
"""

def dimensions():
    return 8, 3

width, height = dimensions()
print("width", width, "height", height)
