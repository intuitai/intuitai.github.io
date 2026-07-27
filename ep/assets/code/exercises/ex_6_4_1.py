"""Exercise 6.4.1 — A list is mutable

Chapter 6: Objects — Everyday Programming

This program corrects a typo in a list of daily temperatures.

This program contains exactly one bug. Solution: sol_6_4_1.py
"""

tokyo_temps = [33.0, 36.5, 31.0]
tokyo_temps[3] = 33.5
print(tokyo_temps)   # [33.5, 36.5, 31.0]
