"""Exercise 6.5.5 — Shallow copy shares inner lists

Chapter 6: Objects — Everyday Programming

The seating chart is a list of rows. We copy it, then add a seat to one
row of the copy; the original chart should be unchanged.

This program contains exactly one bug. Solution: sol_6_5_5.py
"""

import copy

seats = [["A1", "A2"], ["B1", "B2"]]
new_seats = seats.copy()
new_seats[0].append("A3")
print(seats)       # [['A1', 'A2'], ['B1', 'B2']]
print(new_seats)   # [['A1', 'A2', 'A3'], ['B1', 'B2']]
