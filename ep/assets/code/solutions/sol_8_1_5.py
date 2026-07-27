"""Solution 8.1.5 — Greeting by name

Chapter 8: Input and Output — Everyday Programming

Bug type: Syntax

The f-string is missing its closing double quote, so Python never finds
the end of the string and reports a syntax error. Add the closing "
before the parenthesis.

Exercise: ex_8_1_5.py
"""

# Assume the user types: Ava
name = input("What is your name? ")
print(f"Hello, {name}! Welcome aboard.")
