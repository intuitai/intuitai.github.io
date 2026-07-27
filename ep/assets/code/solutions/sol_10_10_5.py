"""Solution 10.10.5 — A lambda with two inputs

Chapter 10: Functions — Everyday Programming

Bug type: Syntax

Lambda parameters must be separated by a comma, so lambda a b: a + b is
a SyntaxError. Write lambda a, b: a + b.

Exercise: ex_10_10_5.py
"""

add = lambda a, b: a + b

print(add(3, 4))  # 7
