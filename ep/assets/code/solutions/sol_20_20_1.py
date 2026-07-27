"""Solution 20.20.1 — Accepting a yes answer

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

"YES" == "yes" is False because case differs. Normalize the case first
with .lower().

Exercise: ex_20_20_1.py
"""

answer = "YES"
if answer.lower() == "yes":
    print("Confirmed")
else:
    print("Not confirmed")
