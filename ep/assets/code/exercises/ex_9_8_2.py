"""Exercise 9.8.2 — Skip one value

Chapter 9: Control Flow — Everyday Programming

This program should print 1, 2, 4, 5, 6, skipping only 3.

This program contains exactly one bug. Solution: sol_9_8_2.py
"""

for number in range(1, 7):
    if number == 3:
        pass
    print(number)
# Expected: 1 2 4 5 6
