"""Exercise 20.23.3 — Checking a measured volume

Chapter 20: Common Pitfalls — Everyday Programming

This program should confirm that three 0.1 L pours fill a 0.3 L cup.

This program contains exactly one bug. Solution: sol_20_23_3.py
"""

pour = 0.1
filled = pour * 3
if filled == 0.3:
    print("Cup is exactly full")
else:
    print("Cup is not exactly full")
