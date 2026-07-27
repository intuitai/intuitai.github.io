"""Exercise 20.21.3 — Greeting each guest

Chapter 20: Common Pitfalls — Everyday Programming

This program should print a greeting for every guest.

This program contains exactly one bug. Solution: sol_20_21_3.py
"""

guests = ["Ana", "Ben", "Cara"]
for guest in range(len(guests)):
    print("Welcome,", guest)
