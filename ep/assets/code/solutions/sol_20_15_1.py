"""Solution 20.15.1 — Reading the current temperature

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

Writing current_temperature without parentheses prints the function
object instead of calling it. Add () to invoke it.

Exercise: ex_20_15_1.py
"""

def current_temperature():
    return 21.5

print("Temperature:", current_temperature())
