"""Solution 20.8.1 — Splitting students into teams

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

/ gives 7.5, but full teams need integer division. Use // to get 7.

Exercise: ex_20_8_1.py
"""

students = 30
team_size = 4
print(students // team_size)  # 7
