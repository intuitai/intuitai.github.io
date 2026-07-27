"""Solution 5.2.5 — Celsius to Fahrenheit

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

Operator precedence makes celsius * 9 / 5 - 32 subtract 32 instead of
adding it, and the +32 must come after the multiply/divide. Add
parentheses or use + 32: the formula is celsius * 9 / 5 + 32.

Exercise: ex_5_2_5.py
"""

celsius = 100.0
fahrenheit = celsius * 9 / 5 + 32
print(fahrenheit)   # 212.0
