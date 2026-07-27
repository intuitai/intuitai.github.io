"""Exercise 5.5.4 — Length of nothing

Chapter 5: Data Structures — Everyday Programming

A list of temperatures has not been filled in yet, so it is None. The
program tries to count it and should instead detect the missing list and
print 0.

This program contains exactly one bug. Solution: sol_5_5_4.py
"""

temps = None
count = len(temps)
print(count)   # 0
