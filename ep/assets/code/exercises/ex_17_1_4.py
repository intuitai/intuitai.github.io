"""Exercise 17.1.4 — Percent of a total

Chapter 17: Testing — Everyday Programming

The function should return what percent part is of whole, and the assert
should pass for 25 out of 50.

This program contains exactly one bug. Solution: sol_17_1_4.py
"""

def percent(part, whole)
    return part / whole * 100

assert percent(25, 50) == 50
print("passed")
