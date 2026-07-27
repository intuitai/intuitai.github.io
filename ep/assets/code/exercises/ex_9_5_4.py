"""Exercise 9.5.4 — Sum of first ten numbers

Chapter 9: Control Flow — Everyday Programming

This program should add the numbers 1 through 10 and print 55.

This program contains exactly one bug. Solution: sol_9_5_4.py
"""

total = 0

for number in range(1, 10):
    total += number

print(total)
# Expected: 55
