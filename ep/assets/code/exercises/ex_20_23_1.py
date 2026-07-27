"""Exercise 20.23.1 — Splitting a bill exactly

Chapter 20: Common Pitfalls — Everyday Programming

This program should confirm that three shares of $0.10 add up to $0.30.

This program contains exactly one bug. Solution: sol_20_23_1.py
"""

share = 0.10
total = share + share + share
if total == 0.30:
    print("The shares add up exactly")
else:
    print("The shares do not add up exactly")
