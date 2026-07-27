"""Solution 10.7.4 — None in arithmetic

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The function never returns total, so it returns None, and None + 5
raises a TypeError. Return the value.

Exercise: ex_10_7_4.py
"""

def base_value():
    total = 10
    return total

print(base_value() + 5)  # 15
