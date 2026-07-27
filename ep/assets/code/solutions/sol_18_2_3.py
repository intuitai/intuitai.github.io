"""Solution 18.2.3 — Doubling a recipe

Chapter 18: Bugs — Everyday Programming

Bug type: Runtime

cups_of_flour is a string, and multiplying a string by a float raises
TypeError. Storing the quantity as a number lets the multiplication
work.

Exercise: ex_18_2_3.py
"""

cups_of_flour = 2.0
doubled = cups_of_flour * 2.0
print(doubled)   # 4.0
