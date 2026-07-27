"""Exercise 16.3.5 — Tax on a purchase

Chapter 16: Handling Failures — Everyday Programming

This program parses a purchase amount and, when it succeeds, computes 8
percent tax in the else block.

This program contains exactly one bug. Solution: sol_16_3_5.py
"""

try:
    amount = float(input("Purchase amount? "))
except ValueError:
    print("That was not a number.")
else:
    tax = amount + 0.08
    print("Tax is", tax)
