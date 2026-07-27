"""Solution 20.7.2 — Doubling a typed quantity

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

cookies is text, so cookies * 2 repeats the string (e.g. "1212") instead
of doubling the number. Convert the input to int first.

Exercise: ex_20_7_2.py
"""

cookies = int(input("How many cookies? "))
print(cookies * 2 == 24)  # for input 12
