"""Exercise 16.4.4 — Final tally

Chapter 16: Handling Failures — Everyday Programming

Whatever happens above, this program must always print Final tally
complete. at the end. With rounds set to 0 it currently does not.

This program contains exactly one bug. Solution: sol_16_4_4.py
"""

points = 90
rounds = 0
try:
    average = points / rounds
    print("Average:", average)
    print("Final tally complete.")
except ZeroDivisionError:
    print("No rounds played.")
