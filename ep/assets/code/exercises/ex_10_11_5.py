"""Exercise 10.11.5 — Checking for None

Chapter 10: Functions — Everyday Programming

The guard should run when no list is passed; both calls should print a
one-item list.

This program contains exactly one bug. Solution: sol_10_11_5.py
"""

def append_day(day, days=None):
    if days == []:
        days = []
    days.append(day)
    return days

print(append_day("Mon"))  # ['Mon']
print(append_day("Tue"))  # ['Tue']
