"""Solution 9.9.2 — Empty function

Chapter 9: Control Flow — Everyday Programming

Bug type: Syntax

A function with an empty body is illegal; Python raises an
IndentationError. Adding pass as the placeholder body fixes it.

Exercise: ex_9_9_2.py
"""

def future_feature():
    pass

future_feature()
print("Done")
