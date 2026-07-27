"""Exercise 5.5.3 — Checking for a value

Chapter 5: Data Structures — Everyday Programming

When a value is None, the program should print "missing".

This program contains exactly one bug. Solution: sol_5_5_3.py
"""

favorite = None

if favorite is not None:
    print("missing")
else:
    print("has value")
# expected: missing
