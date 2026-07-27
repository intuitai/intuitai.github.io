"""Exercise 20.23.5 — Comparing a savings target

Chapter 20: Common Pitfalls — Everyday Programming

This program should confirm that saving $1.10 three times reaches $3.30.

This program contains exactly one bug. Solution: sol_20_23_5.py
"""

weekly = 1.10
saved = weekly * 3
if saved == 3.30:
    print("You reached the target")
else:
    print("You did not reach the target")
