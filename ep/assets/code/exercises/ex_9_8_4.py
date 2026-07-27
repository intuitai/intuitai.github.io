"""Exercise 9.8.4 — Skip the indentation

Chapter 9: Control Flow — Everyday Programming

This program should print every odd number from 1 to 6, skipping the
even ones.

This program contains exactly one bug. Solution: sol_9_8_4.py
"""

for number in range(1, 7):
    if number % 2 == 0:
    continue
    print(number)
# Expected: 1 3 5
