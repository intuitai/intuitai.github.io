"""Solution 5.3.4 — Empty cart

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

is_empty = items = 0 is a chained assignment that sets is_empty to 0,
not the comparison you intended; it runs but prints 0. Comparing values
needs ==, so write is_empty = items == 0.

Exercise: ex_5_3_4.py
"""

items = 0
is_empty = items == 0
print(is_empty)   # True
