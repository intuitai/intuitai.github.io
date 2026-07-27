"""Exercise 7.5.3 — Missing value check

Chapter 7: Operators — Everyday Programming

This program should report that a measurement is missing (its value is
None) and print True.

This program contains exactly one bug. Solution: sol_7_5_3.py
"""

measurement = None
is_missing = measurement is not None
print(is_missing)   # expected: True
