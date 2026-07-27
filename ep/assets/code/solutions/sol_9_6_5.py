"""Solution 9.6.5 — Sum until limit

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

number is incremented *before* being added, so the loop adds 2+3+4+5 =
14 and skips 1. Adding first, then incrementing, sums 1+2+3+4 = 10.

Exercise: ex_9_6_5.py
"""

total = 0
number = 1

while total < 10:
    total += number
    number += 1

print(total)
