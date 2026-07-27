"""Solution 18.1.2 — Tip calculator

Chapter 18: Bugs — Everyday Programming

Bug type: Syntax

The opening parenthesis after bill * is never closed, leaving an
unbalanced bracket that the parser rejects. Closing the parenthesis
fixes the expression.

Exercise: ex_18_1_2.py
"""

bill = 40.0
tip_rate = 0.15
total = bill + (bill * tip_rate)
print(total)   # 46.0
