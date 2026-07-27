"""Solution 20.2.2 — Inconsistent indentation in a loop

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

The final print is indented more deeply than the loop body, which Python
reads as an unexpected indent. Aligning it at the outer level (after the
loop) fixes it.

Exercise: ex_20_2_2.py
"""

rainfall = [12, 8, 15]
total = 0
for amount in rainfall:
    total = total + amount
print(total)  # 35
