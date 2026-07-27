"""Solution 7.1.1 — Average of three test scores

Chapter 7: Operators — Everyday Programming

Bug type: Logical

Because / has higher precedence than +, only score3 is divided by 3, so
the answer is wrong. Wrap the sum in parentheses so the division applies
to the whole total.

Exercise: ex_7_1_1.py
"""

score1 = 78
score2 = 85
score3 = 89
average = (score1 + score2 + score3) / 3
print(average)   # 84.0
