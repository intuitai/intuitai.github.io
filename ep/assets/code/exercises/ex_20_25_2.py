"""Exercise 20.25.2 — Backing up monthly budgets

Chapter 20: Common Pitfalls — Everyday Programming

The program should make an independent copy of a nested budget so
changes do not leak back.

This program contains exactly one bug. Solution: sol_20_25_2.py
"""

import copy

budgets = [[100, 200], [300, 400]]
saved = budgets[:]
saved[1][0] = 999
print("Budgets:", budgets)  # Budgets: [[100, 200], [300, 400]]
