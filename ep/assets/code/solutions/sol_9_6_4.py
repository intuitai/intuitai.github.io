"""Solution 9.6.4 — Loop condition

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

while count < 5 stops after printing 4, so 5 is never reached. Use <= to
include 5.

Exercise: ex_9_6_4.py
"""

count = 1

while count <= 5:
    print(count)
    count += 1
