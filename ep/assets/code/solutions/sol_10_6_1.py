"""Solution 10.6.1 — Returning a pair

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The function returns a single value, so unpacking into two names raises
a ValueError. Return both min and max as a pair.

Exercise: ex_10_6_1.py
"""

def min_max(a, b, c):
    return min(a, b, c), max(a, b, c)

low, high = min_max(31.0, 36.5, 33.0)
print(low, high)  # 31.0 36.5
