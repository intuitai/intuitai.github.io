"""Solution 10.4.1 — A default value

Chapter 10: Functions — Everyday Programming

Bug type: Logical

greet without parentheses does not call the function. Add () so it runs
with the default name.

Exercise: ex_10_4_1.py
"""

def greet(name="friend"):
    print("Hello,", name)

greet()
