"""Solution 7.2.3 — Doubling a recipe

Chapter 7: Operators — Everyday Programming

Bug type: Runtime

The variable is cups_flour, but print refers to Cups_flour with a
capital C, raising a NameError. Match the name exactly.

Exercise: ex_7_2_3.py
"""

cups_flour = 2
cups_flour *= 2
print(cups_flour)   # 4
