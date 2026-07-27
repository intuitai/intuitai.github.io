"""Exercise 20.20.1 — Accepting a yes answer

Chapter 20: Common Pitfalls — Everyday Programming

This program should accept the answer "yes" no matter how it is
capitalized.

This program contains exactly one bug. Solution: sol_20_20_1.py
"""

answer = "YES"
if answer == "yes":
    print("Confirmed")
else:
    print("Not confirmed")
