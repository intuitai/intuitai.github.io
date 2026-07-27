"""Solution 9.3.2 — Weekend check

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

A day cannot equal both Saturday and Sunday, so the and condition is
never true and nothing prints. The cases are alternatives, so use or.

Exercise: ex_9_3_2.py
"""

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Relax")
# expected: Relax
