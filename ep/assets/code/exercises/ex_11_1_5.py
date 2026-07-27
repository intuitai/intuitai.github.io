"""Exercise 11.1.5 — global list, read inside the function

Chapter 11: Scoping — Everyday Programming

This program should print the average of a global list of test scores.

This program contains exactly one bug. Solution: sol_11_1_5.py
"""

scores = [80, 90, 100]

def average()
    return sum(scores) / len(scores)

print("Average:", average())
# Expected:
# Average: 90.0
