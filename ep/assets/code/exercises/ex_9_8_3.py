"""Exercise 9.8.3 — Sum positive numbers

Chapter 9: Control Flow — Everyday Programming

This program should add only the positive numbers and print 9.

This program contains exactly one bug. Solution: sol_9_8_3.py
"""

numbers = [4, -2, 5, -1]
total = 0

for number in numbers:
    if number < 0:
        continue
    total += number
    continue

print(total + 1)
# Expected: 9
