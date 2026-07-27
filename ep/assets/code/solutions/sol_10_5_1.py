"""Solution 10.5.1 — Calling by name

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

grade=7 is an unexpected keyword argument the function does not accept,
raising a TypeError. Pass only name and age.

Exercise: ex_10_5_1.py
"""

def introduce(name, age):
    print(name, "is", age, "years old")

introduce(name="Lina", age=12)
