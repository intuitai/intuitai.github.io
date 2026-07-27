"""Solution 9.8.5 — Skip a specific student

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

The condition skips everyone *except* Leo, so only Leo is printed—the
opposite of what we want. Skip when the name *is* Leo by using ==.

Exercise: ex_9_8_5.py
"""

names = ["Ana", "Leo", "Sam"]

for name in names:
    if name == "Leo":
        continue
    print(name)
