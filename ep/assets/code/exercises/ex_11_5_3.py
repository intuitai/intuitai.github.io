"""Exercise 11.5.3 — nonlocal keyword

Chapter 11: Scoping — Everyday Programming

This program tracks the highest reading seen so far using nonlocal, and
should print 9 after two readings.

This program contains exactly one bug. Solution: sol_11_5_3.py
"""

def make_tracker():
    highest = 0

    def record(value):
        nonlocal highest
        if value > highest:
            highest = value
        return highest

    return record

record = make_tracker()
record(4)
print("Highest:", record(9)
# Expected:
# Highest: 9
