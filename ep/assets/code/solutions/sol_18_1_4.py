"""Solution 18.1.4 — Weekly distance

Chapter 18: Bugs — Everyday Programming

Bug type: Syntax

There is a missing operator (or comma) between tuesday and wednesday;
two names sitting side by side cannot be parsed. Adding the + sums all
three days.

Exercise: ex_18_1_4.py
"""

monday = 3.2
tuesday = 4.1
wednesday = 2.7
total = monday + tuesday + wednesday
print(total)   # 10.0
