"""Exercise 10.7.1 — No return means None

Chapter 10: Functions — Everyday Programming

This program prints a message, and the returned value should be None.

This program contains exactly one bug. Solution: sol_10_7_1.py
"""

def announce():
    print("The meeting starts now.")
    return "done"

result = announce()
print(result)  # None
