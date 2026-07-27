"""Solution 10.11.1 — The shared default list

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The default list is created once and shared across calls, so it keeps
growing. Use None as the default and build a fresh list inside.

Exercise: ex_10_11_1.py
"""

def collect(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(collect("apple"))   # ['apple']
print(collect("bread"))   # ['bread']
