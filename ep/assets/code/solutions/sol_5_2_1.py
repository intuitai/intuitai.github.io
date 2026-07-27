"""Solution 5.2.1 — Average temperature

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

Without parentheses, only reading3 / 3 is divided (operator precedence),
so the sum is wrong. Wrap the addition in parentheses before dividing.

Exercise: ex_5_2_1.py
"""

reading1 = 20.0
reading2 = 22.0
reading3 = 24.0

average = (reading1 + reading2 + reading3) / 3
print(average)   # 22.0
