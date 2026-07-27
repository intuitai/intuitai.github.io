"""Solution 6.5.3 — Copying with a slice

Chapter 6: Objects — Everyday Programming

Bug type: Logical

The slice grades[0:2] copies only the first two items, so working starts
as [85, 90] and the result is wrong. A full-list slice grades[:] copies
every element.

Exercise: ex_6_5_3.py
"""

grades = [85, 90, 78]
working = grades[:]
working.append(100)
print(grades)    # [85, 90, 78]
print(working)   # [85, 90, 78, 100]
