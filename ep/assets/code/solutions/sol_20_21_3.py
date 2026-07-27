"""Solution 20.21.3 — Greeting each guest

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

range(len(guests)) yields the numbers 0, 1, 2, so the greeting prints
numbers, not names. Iterate over the guests directly.

Exercise: ex_20_21_3.py
"""

guests = ["Ana", "Ben", "Cara"]
for guest in guests:
    print("Welcome,", guest)
