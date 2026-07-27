"""Solution 7.3.5 — Within speed limit

Chapter 7: Operators — Everyday Programming

Bug type: Logical

A speed of exactly 65 is within the limit, but < excludes it and gives
False. Use <= to include the limit itself.

Exercise: ex_7_3_5.py
"""

speed = 65
limit = 65
within_limit = speed <= limit
print(within_limit)   # True
