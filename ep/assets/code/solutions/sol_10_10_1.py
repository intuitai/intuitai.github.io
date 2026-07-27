"""Solution 10.10.1 — Lambda syntax

Chapter 10: Functions — Everyday Programming

Bug type: Syntax

A lambda body is a single expression and cannot contain return, so
lambda x: return x * x is a SyntaxError. Drop the return.

Exercise: ex_10_10_1.py
"""

square = lambda x: x * x

print(square(5))  # 25
