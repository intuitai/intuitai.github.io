"""Exercise 20.25.4 — Snapshotting weekly readings

Chapter 20: Common Pitfalls — Everyday Programming

The program should take a snapshot of nested sensor readings that stays
fixed.

This program contains exactly one bug. Solution: sol_20_25_4.py
"""

import copy

readings = [[1.0, 2.0], [3.0, 4.0]]
snapshot = readings.copy()
snapshot[0][0] = 99.0
print("Readings:", readings)  # Readings: [[1.0, 2.0], [3.0, 4.0]]
