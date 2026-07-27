"""Exercise 9.7.5 — Stop at zero

Chapter 9: Control Flow — Everyday Programming

This program should print readings until it hits a 0, then stop. It
should print 5 and 8.

This program contains exactly one bug. Solution: sol_9_7_5.py
"""

readings = [5, 8, 0, 3]

for reading in readings:
    if reading == 0:
        continue
    print(reading)
# Expected: 5 8
