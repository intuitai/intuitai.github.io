"""Solution 10.5.4 — Keyword after positional

Chapter 10: Functions — Everyday Programming

Bug type: Syntax

A positional argument cannot follow a keyword argument, so
score_line(name="Sam", 95) is a SyntaxError. Either make both keywords
or both positional.

Exercise: ex_10_5_4.py
"""

def score_line(name, points):
    print(name, "scored", points)

score_line(name="Sam", points=95)
