"""Solution 9.1.2 — Temperature category

Chapter 9: Control Flow — Everyday Programming

Bug type: Syntax

The body of the first if is not indented, so Python raises an
IndentationError. Indenting the print four spaces fixes it.

Exercise: ex_9_1_2.py
"""

temp_c = 36.5

if temp_c > 35:
    print("Heat warning")
elif temp_c < 0:
    print("Freezing")
else:
    print("Normal")
