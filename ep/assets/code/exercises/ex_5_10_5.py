"""Exercise 5.10.5 — Whole-number average

Chapter 5: Data Structures — Everyday Programming

Two test scores are 80 and 91. The program should print their average as
a whole number, 85.

This program contains exactly one bug. Solution: sol_5_10_5.py
"""

score1 = 80
score2 = 91

average = str((score1 + score2) / 2)
print(int(average))   # 85
