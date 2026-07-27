"""Solution 10.12.5 — Sharing the same object

Chapter 10: Functions — Everyday Programming

Bug type: Logical

items = list(items) makes a separate copy, so the append affects only
the copy and the caller's list is unchanged. Append directly to the
passed-in list.

Exercise: ex_10_12_5.py
"""

def append_value(items, value):
    items.append(value)

box = [1, 2, 3]
append_value(box, 4)
print(box)  # [1, 2, 3, 4]
