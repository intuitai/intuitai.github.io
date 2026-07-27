"""Solution 9.5.1 — Counting to five

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

range stops before its end value, so range(1, 5) yields 1–4. To reach 5,
use range(1, 6).

Exercise: ex_9_5_1.py
"""

for number in range(1, 6):
    print(number)
