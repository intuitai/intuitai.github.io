"""Solution 6.5.5 — Shallow copy shares inner lists

Chapter 6: Objects — Everyday Programming

Bug type: Logical

seats.copy() is a shallow copy: the outer list is new, but the row lists
are shared, so new_seats[0].append also changes seats. Using
copy.deepcopy copies each row, leaving the original chart unchanged.

Exercise: ex_6_5_5.py
"""

import copy

seats = [["A1", "A2"], ["B1", "B2"]]
new_seats = copy.deepcopy(seats)
new_seats[0].append("A3")
print(seats)       # [['A1', 'A2'], ['B1', 'B2']]
print(new_seats)   # [['A1', 'A2', 'A3'], ['B1', 'B2']]
