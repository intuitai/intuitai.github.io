"""Solution 20.7.3 — Summing two typed numbers

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

second is left as text, so first + second adds an int and a string,
raising TypeError. Convert second with int() as well.

Exercise: ex_20_7_3.py
"""

first = int(input("First price: "))
second = int(input("Second price: "))
print(first + second)
