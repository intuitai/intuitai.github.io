"""Solution 5.1.2 — Students per team

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

The / operator always produces a float (6.0), but a whole number of
students per team is wanted. Use integer division // to get the int 6.

Exercise: ex_5_1_2.py
"""

students = 30
teams = 5

per_team = students // teams
print(per_team)   # 6
