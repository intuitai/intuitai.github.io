"""Solution 10.8.1 — Triple quotes

Chapter 10: Functions — Everyday Programming

Bug type: Syntax

The string opens with a single double-quote but closes with triple
single-quotes, so the quotes do not match and Python raises a
SyntaxError. Use matching triple quotes.

Exercise: ex_10_8_1.py
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add(2, 3))  # 5
