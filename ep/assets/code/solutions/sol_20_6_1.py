"""Solution 20.6.1 — Joining text and a number

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

You cannot add a string to an integer; "Steps today: " + steps raises
TypeError. Convert the number with str().

Exercise: ex_20_6_1.py
"""

steps = 8000
print("Steps today: " + str(steps))
