"""Exercise 6.5.1 — Assignment is not a copy

Chapter 6: Objects — Everyday Programming

The backup should stay unchanged after we add a new reading to the
original.

This program contains exactly one bug. Solution: sol_6_5_1.py
"""

temps = [33.0, 36.5, 31.0]
backup = temps
temps.append(34.0)
print(backup)   # [33.0, 36.5, 31.0]
