"""Exercise 10.9.5 — Order of args and kwargs

Chapter 10: Functions — Everyday Programming

This should print both the positional tuple and the keyword dictionary.

This program contains exactly one bug. Solution: sol_10_9_5.py
"""

def collect(**kwargs, *args):
    print(args)
    print(kwargs)

collect(1, 2, unit="cm")
