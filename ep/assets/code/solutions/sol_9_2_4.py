"""Solution 9.2.4 — Speed limit check

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

“At most 60” includes 60, but < excludes it, so a car at the limit is
wrongly flagged. Use <=.

Exercise: ex_9_2_4.py
"""

speed = 60
limit = 60

if speed <= limit:
    print("OK")
else:
    print("Too fast")
