"""Exercise 9.3.2 — Weekend check

Chapter 9: Control Flow — Everyday Programming

This program should print Relax on Saturday or Sunday. For "Saturday" it
should print Relax.

This program contains exactly one bug. Solution: sol_9_3_2.py
"""

day = "Saturday"

if day == "Saturday" and day == "Sunday":
    print("Relax")
# expected: Relax
