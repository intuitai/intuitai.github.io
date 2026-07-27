"""Solution 5.4.3 — Full name

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

Concatenation does not insert a space, so the result is "MayaSingh". Add
a space string between the names.

Exercise: ex_5_4_3.py
"""

first = "Maya"
last = "Singh"

full = first + " " + last
print(full)   # Maya Singh
