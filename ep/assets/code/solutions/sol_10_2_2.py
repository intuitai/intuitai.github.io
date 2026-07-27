"""Solution 10.2.2 — Parameter order

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The arguments are passed in the wrong order, so name becomes 15 and age
becomes "Maya". Pass the name first, then the age.

Exercise: ex_10_2_2.py
"""

def describe(name, age):
    print(name, "is", age, "years old")

describe("Maya", 15)
