"""Exercise 9.2.2 — Freezing point

Chapter 9: Control Flow — Everyday Programming

Water freezes at 0 degrees Celsius or below. This program should print
Frozen for a temperature of 0.

This program contains exactly one bug. Solution: sol_9_2_2.py
"""

temp_c = 0

if temp_c < 0:
    print("Frozen")
else:
    print("Liquid")
# Expected: Frozen
