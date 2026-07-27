"""Solution 6.4.1 — A list is mutable

Chapter 6: Objects — Everyday Programming

Bug type: Runtime

The list has three items at indexes 0, 1, and 2, so tokyo_temps[3] is
out of range and raises an IndexError. The typo is at index 0, so the
fix assigns to tokyo_temps[0].

Exercise: ex_6_4_1.py
"""

tokyo_temps = [33.0, 36.5, 31.0]
tokyo_temps[0] = 33.5
print(tokyo_temps)   # [33.5, 36.5, 31.0]
