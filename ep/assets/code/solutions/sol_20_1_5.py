"""Solution 20.1.5 — Missing colon after elif

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

Like if, an elif header requires a trailing :. Adding it lets the three-
way branch parse.

Exercise: ex_20_1_5.py
"""

score = 55
if score >= 60:
    print("Pass")
elif score >= 50:
    print("Borderline")
else:
    print("Fail")
