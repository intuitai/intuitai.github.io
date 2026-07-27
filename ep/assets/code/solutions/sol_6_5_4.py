"""Solution 6.5.4 — Deep copy for nested lists

Chapter 6: Objects — Everyday Programming

Bug type: Logical

copy.copy makes a shallow copy, so the inner lists are still shared and
appending to independent[0] also changes grid. copy.deepcopy copies the
nested lists recursively, keeping the original intact.

Exercise: ex_6_5_4.py
"""

import copy

grid = [[1, 2], [3, 4]]
independent = copy.deepcopy(grid)
independent[0].append(99)
print(grid)         # [[1, 2], [3, 4]]
print(independent)  # [[1, 2, 99], [3, 4]]
