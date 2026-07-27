"""Exercise 6.5.3 — Copying with a slice

Chapter 6: Objects — Everyday Programming

A slice copy of a flat list should leave the original alone.

This program contains exactly one bug. Solution: sol_6_5_3.py
"""

grades = [85, 90, 78]
working = grades[0:2]
working.append(100)
print(grades)    # [85, 90, 78]
print(working)   # [85, 90, 78, 100]
