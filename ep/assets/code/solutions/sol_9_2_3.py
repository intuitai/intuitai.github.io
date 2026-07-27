"""Solution 9.2.3 — Not equal

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

The condition should test “not 0” but uses ==, so it prints Sold out
exactly when seats is 0. Use != to match the intended meaning.

Exercise: ex_9_2_3.py
"""

seats_left = 0

if seats_left != 0:
    print("Sold out")
