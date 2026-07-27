"""Solution 9.5.4 — Sum of first ten numbers

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

range(1, 10) stops at 9, so 10 is left out and the total is 45. Use
range(1, 11) to include 10.

Exercise: ex_9_5_4.py
"""

total = 0

for number in range(1, 11):
    total += number

print(total)
