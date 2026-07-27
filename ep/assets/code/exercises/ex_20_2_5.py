"""Exercise 20.2.5 — Indentation mixing two blocks

Chapter 20: Common Pitfalls — Everyday Programming

This program should print each grade and then announce the report is
finished.

This program contains exactly one bug. Solution: sol_20_2_5.py
"""

grades = [88, 91, 79]
for grade in grades:
    print(grade)
  print("Report complete")
