"""Exercise 20.20.2 — Matching a chosen color

Chapter 20: Common Pitfalls — Everyday Programming

The program should detect the favorite color "blue" regardless of case.

This program contains exactly one bug. Solution: sol_20_20_2.py
"""

favorite = "Blue"
if favorite.upper() == "blue":
    print("You picked blue")
