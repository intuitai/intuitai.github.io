"""Solution 5.3.5 — Within speed limit

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

Being within the limit means the speed is at or below it, but > tests
the opposite. Use <= so 60 within 65 gives True.

Exercise: ex_5_3_5.py
"""

speed = 60
limit = 65

within_limit = speed <= limit
print(within_limit)   # True
