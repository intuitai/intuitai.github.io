"""Solution 10.8.2 — Docstring placement

Chapter 10: Functions — Everyday Programming

Bug type: Logical

A string becomes the docstring only when it is the first statement in
the body; here it sits after an assignment, so __doc__ is None. Move the
docstring to the top.

Exercise: ex_10_8_2.py
"""

def to_meters(feet):
    """Convert feet to meters."""
    result = feet * 0.3048
    return result

print(to_meters.__doc__)  # Convert feet to meters.
