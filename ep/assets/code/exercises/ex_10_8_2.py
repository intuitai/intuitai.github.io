"""Exercise 10.8.2 — Docstring placement

Chapter 10: Functions — Everyday Programming

The docstring should sit directly under the def line so it becomes the
function's documentation.

This program contains exactly one bug. Solution: sol_10_8_2.py
"""

def to_meters(feet):
    result = feet * 0.3048
    """Convert feet to meters."""
    return result

print(to_meters.__doc__)  # Convert feet to meters.
