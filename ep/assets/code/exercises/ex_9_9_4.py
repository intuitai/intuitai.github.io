"""Exercise 9.9.4 — Placeholder branch

Chapter 9: Control Flow — Everyday Programming

For now, negative readings should be ignored (handled later) while
others are printed. With this data it should print 5 and 8.

This program contains exactly one bug. Solution: sol_9_9_4.py
"""

readings = [5, -3, 8]

for reading in readings:
    if reading < 0:
        pass
        print(reading)
    else:
        print(reading)
# Expected: 5 8
