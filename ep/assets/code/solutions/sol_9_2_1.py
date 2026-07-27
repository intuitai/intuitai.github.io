"""Solution 9.2.1 — Exact match

Chapter 9: Control Flow — Everyday Programming

Bug type: Syntax

A single = is assignment, not comparison, and is not allowed in an if
condition. Use == to compare.

Exercise: ex_9_2_1.py
"""

answer = 42

if answer == 42:
    print("Correct")
else:
    print("Try again")
