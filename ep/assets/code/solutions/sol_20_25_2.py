"""Solution 20.25.2 — Backing up monthly budgets

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

Slicing with [:] copies only the outer list; the nested lists stay
shared, so editing saved edits budgets. Use copy.deepcopy.

Exercise: ex_20_25_2.py
"""

import copy

budgets = [[100, 200], [300, 400]]
saved = copy.deepcopy(budgets)
saved[1][0] = 999
print("Budgets:", budgets)  # Budgets: [[100, 200], [300, 400]]
