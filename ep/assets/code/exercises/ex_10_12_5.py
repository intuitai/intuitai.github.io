"""Exercise 10.12.5 — Sharing the same object

Chapter 10: Functions — Everyday Programming

Both names point to the same list, so the append should be visible
outside; this prints a 4-item list.

This program contains exactly one bug. Solution: sol_10_12_5.py
"""

def append_value(items, value):
    items = list(items)
    items.append(value)

box = [1, 2, 3]
append_value(box, 4)
print(box)  # [1, 2, 3, 4]
