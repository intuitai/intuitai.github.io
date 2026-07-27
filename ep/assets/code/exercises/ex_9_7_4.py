"""Exercise 9.7.4 — First even number

Chapter 9: Control Flow — Everyday Programming

This program should print the first even number in the list and stop.
For these numbers it should print 4.

This program contains exactly one bug. Solution: sol_9_7_4.py
"""

numbers = [3, 7, 4, 6]

for number in numbers:
    if number % 2 == 0:
        break
        print(number)
# Expected: 4
