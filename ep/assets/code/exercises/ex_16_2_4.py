"""Exercise 16.2.4 — Looking up a grade

Chapter 16: Handling Failures — Everyday Programming

This program looks up a student's grade in a dictionary and reports a
clear message if the name is missing.

This program contains exactly one bug. Solution: sol_16_2_4.py
"""

grades = {"Ann": 91, "Bo": 84}
name = "Cleo"
try:
    print(name, "scored", grades[name])
except ValueError:
    print("No grade recorded for", name)
