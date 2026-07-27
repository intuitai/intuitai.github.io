"""Solution 20.13.3 — Replacing a digit in a code

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Strings are immutable, so code[0] = "9" raises TypeError. Construct a
new string.

Exercise: ex_20_13_3.py
"""

code = "12345"
code = "9" + code[1:]
print(code)
