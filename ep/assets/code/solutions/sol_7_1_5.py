"""Solution 7.1.5 — Total cost with tax

Chapter 7: Operators — Everyday Programming

Bug type: Syntax

The call to print is missing its closing parenthesis, so the program
will not parse. Add the ).

Exercise: ex_7_1_5.py
"""

price = 20
tax_rate = 0.10
total = price + price * tax_rate
print(total)   # 22.0
