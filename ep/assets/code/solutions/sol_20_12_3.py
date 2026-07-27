"""Solution 20.12.3 — A list of temperatures

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Parentheses make a tuple, which is immutable, so temperatures[0] = 19
raises TypeError. Use brackets to make an editable list.

Exercise: ex_20_12_3.py
"""

temperatures = [21, 22, 20]
temperatures[0] = 19
print(temperatures)
