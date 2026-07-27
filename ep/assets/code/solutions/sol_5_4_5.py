"""Solution 5.4.5 — Last three characters

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

code[-3] is a single character ("7"), not the last three. Slice with
code[-3:] to get "789".

Exercise: ex_5_4_5.py
"""

code = "ABC789"
last_three = code[-3:]
print(last_three)   # 789
