"""Solution 10.4.5 — The default is optional

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The first parameter value has no default, so calling increase() with no
arguments raises a TypeError. Pass a value, or give value a default.

Exercise: ex_10_4_5.py
"""

def increase(value=0, by=10):
    return value + by

print(increase())  # 10
