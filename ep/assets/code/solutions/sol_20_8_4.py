"""Solution 20.8.4 — Whole minutes from seconds

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

200 / 60 is 3.33...; whole minutes need //, giving 3.

Exercise: ex_20_8_4.py
"""

seconds = 200
minutes = seconds // 60
print(minutes)  # 3
