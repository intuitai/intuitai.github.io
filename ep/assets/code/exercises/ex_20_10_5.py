"""Exercise 20.10.5 — Appending a measurement

Chapter 20: Common Pitfalls — Everyday Programming

This program should add one more pH reading to the list.

This program contains exactly one bug. Solution: sol_20_10_5.py
"""

ph_values = [7.0, 6.8, 7.2]
ph_values[3] = 6.9
print(ph_values)
