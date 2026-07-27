"""Solution 20.19.1 — Converting a typed age

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The bare except: hides every error, including programming mistakes.
Catch only ValueError, which is the error int() raises on bad text.

Exercise: ex_20_19_1.py
"""

text = "12y"
try:
    age = int(text)
    print("Next year you will be", age + 1)
except ValueError:
    print("Please type a whole number")
