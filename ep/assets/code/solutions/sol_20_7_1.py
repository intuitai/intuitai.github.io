"""Solution 20.7.1 — Adding to raw input

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

input() returns text, so year + 1 adds a string and an int, raising
TypeError. Wrap the input in int().

Exercise: ex_20_7_1.py
"""

year = int(input("Enter the year: "))
print(year + 1)
