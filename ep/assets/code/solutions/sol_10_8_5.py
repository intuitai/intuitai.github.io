"""Solution 10.8.5 — Docstring, then code

Chapter 10: Functions — Everyday Programming

Bug type: Syntax

The triple-quoted docstring is opened with \"\"\" but never closed, so
Python reads the rest of the file as one unterminated string and reports
a syntax error. Close the docstring on the same line.

Exercise: ex_10_8_5.py
"""

def kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

print(kelvin.__doc__)   # Convert Celsius to Kelvin.
