"""Exercise 9.7.1 — Stop at the target

Chapter 9: Control Flow — Everyday Programming

This program should print numbers from 1 and stop *before* printing 3,
so it prints 1 and 2.

This program contains exactly one bug. Solution: sol_9_7_1.py
"""

for number in range(1, 6):
    if number == 3:
        continue
    print(number)
# Expected: 1 2
