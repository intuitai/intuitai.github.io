"""Exercise 10.9.1 — Collecting positionals

Chapter 10: Functions — Everyday Programming

This program should sum any number of grades passed in; here the total
should be 270.

This program contains exactly one bug. Solution: sol_10_9_1.py
"""

def total(args):
    return sum(args)

print(total(90, 85, 95))  # 270
