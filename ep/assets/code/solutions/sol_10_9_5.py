"""Solution 10.9.5 — Order of args and kwargs

Chapter 10: Functions — Everyday Programming

Bug type: Syntax

kwargs must come after *args in the definition, so def collect(kwargs,
*args) is a SyntaxError. Put *args first.

Exercise: ex_10_9_5.py
"""

def collect(*args, **kwargs):
    print(args)
    print(kwargs)

collect(1, 2, unit="cm")
