"""Exercise 10.11.1 — The shared default list

Chapter 10: Functions — Everyday Programming

Each call should start with a fresh list, so both lines print a single-
item list.

This program contains exactly one bug. Solution: sol_10_11_1.py
"""

def collect(item, basket=[]):
    basket.append(item)
    return basket

print(collect("apple"))   # ['apple']
print(collect("bread"))   # ['bread']
