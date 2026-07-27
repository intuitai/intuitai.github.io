"""Solution 6.5.1 — Assignment is not a copy

Chapter 6: Objects — Everyday Programming

Bug type: Logical

backup = temps makes both names point at the same list, so appending to
temps also changes backup. Taking a real copy with temps.copy() (or
temps[:]) keeps the backup unchanged.

Exercise: ex_6_5_1.py
"""

temps = [33.0, 36.5, 31.0]
backup = temps.copy()
temps.append(34.0)
print(backup)   # [33.0, 36.5, 31.0]
