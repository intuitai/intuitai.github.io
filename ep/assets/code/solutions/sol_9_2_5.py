"""Solution 9.2.5 — Adult check

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

“18 or older” includes 18, but > excludes it. Use >=.

Exercise: ex_9_2_5.py
"""

age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
