"""Exercise 6.4.2 — Aliasing a list

Chapter 6: Objects — Everyday Programming

The two names are meant to refer to the same list, so a change through
one is seen through the other. This should print the list with the new
reading.

This program contains exactly one bug. Solution: sol_6_4_2.py
"""

readings = [12, 15, 9]
same_readings = list(readings)
same_readings.append(20)
print(readings)   # [12, 15, 9, 20]
