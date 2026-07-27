"""Exercise 6.5.4 — Deep copy for nested lists

Chapter 6: Objects — Everyday Programming

The grid holds rows of numbers. We want an independent copy whose rows
can change without touching the original.

This program contains exactly one bug. Solution: sol_6_5_4.py
"""

import copy

grid = [[1, 2], [3, 4]]
independent = copy.copy(grid)
independent[0].append(99)
print(grid)         # [[1, 2], [3, 4]]
print(independent)  # [[1, 2, 99], [3, 4]]
