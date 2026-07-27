"""Solution 10.3.4 — Return what was asked

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The else branch returns a instead of b, so the larger value is never
returned when b is bigger. Return b in the else branch.

Exercise: ex_10_3_4.py
"""

def larger(a, b):
    if a > b:
        return a
    else:
        return b

print(larger(4, 9))  # 9
