"""Solution 5.10.5 — Whole-number average

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

average is wrapped in str(), so int("85.5") raises a ValueError. Keep
the average numeric and apply int() directly.

Exercise: ex_5_10_5.py
"""

score1 = 80
score2 = 91

average = (score1 + score2) / 2
print(int(average))   # 85
