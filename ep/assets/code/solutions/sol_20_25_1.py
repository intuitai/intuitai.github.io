"""Solution 20.25.1 — Copying a seating chart

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

original.copy() is a shallow copy: the inner row lists are still shared,
so appending through backup also changes original. Use copy.deepcopy.

Exercise: ex_20_25_1.py
"""

import copy

original = [["Ana", "Ben"], ["Cara", "Dan"]]
backup = copy.deepcopy(original)
backup[0].append("Eve")
print("Original:", original)  # Original: [['Ana', 'Ben'], ['Cara', 'Dan']]
