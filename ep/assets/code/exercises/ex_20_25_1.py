"""Exercise 20.25.1 — Copying a seating chart

Chapter 20: Common Pitfalls — Everyday Programming

This program should copy a seating chart so editing the copy leaves the
original unchanged.

This program contains exactly one bug. Solution: sol_20_25_1.py
"""

import copy

original = [["Ana", "Ben"], ["Cara", "Dan"]]
backup = original.copy()
backup[0].append("Eve")
print("Original:", original)  # Original: [['Ana', 'Ben'], ['Cara', 'Dan']]
