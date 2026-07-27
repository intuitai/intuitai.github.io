"""Exercise 9.11.3 — First match returns

Chapter 9: Control Flow — Everyday Programming

This function should return the first number greater than 10, or None.
For this list it should print 15.

This program contains exactly one bug. Solution: sol_9_11_3.py
"""

def first_big(numbers):
    for number in numbers:
        if number > 10:
            print(number)

print(first_big([4, 15, 22]))
# Expected: 15
