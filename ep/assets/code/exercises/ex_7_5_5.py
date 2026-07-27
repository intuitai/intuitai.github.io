"""Exercise 7.5.5 — Day in the schedule

Chapter 7: Operators — Everyday Programming

This program should report whether "Wednesday" is in the schedule and
print True.

This program contains exactly one bug. Solution: sol_7_5_5.py
"""

schedule = ["Monday", "Wednesday", "Friday"]
has_wednesday = "Wednesday" not in schedule
print(has_wednesday)   # expected: True
