"""Solution 7.3.1 — Passing grade check

Chapter 7: Operators — Everyday Programming

Bug type: Logical

A score of exactly 60 should pass, but > excludes 60 and gives False.
Use >= to include the boundary.

Exercise: ex_7_3_1.py
"""

score = 60
passing = score >= 60
print(passing)   # True
