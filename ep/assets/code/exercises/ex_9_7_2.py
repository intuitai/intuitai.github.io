"""Exercise 9.7.2 — First over budget

Chapter 9: Control Flow — Everyday Programming

This program should print the first expense that is over 100 and then
stop.

This program contains exactly one bug. Solution: sol_9_7_2.py
"""

expenses = [40, 80, 150, 90]

for expense in expenses:
    if expense > 100:
        print("Over budget:", expense)
    break
# Expected: Over budget: 150
