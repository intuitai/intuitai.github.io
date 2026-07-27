"""Solution 9.11.1 — Even check

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

The function computes number % 2 == 0 but never returns it, so it
returns None. Adding return sends the result back.

Exercise: ex_9_11_1.py
"""

def is_even(number):
    return number % 2 == 0

print(is_even(4))
