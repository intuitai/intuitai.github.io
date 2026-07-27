"""Solution 10.8.3 — Reading the docstring

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The attribute is __doc__, not __docs__, so accessing it raises an
AttributeError. Use the correct name.

Exercise: ex_10_8_3.py
"""

def half(number):
    """Return half of a number."""
    return number / 2

print(half.__doc__)
