"""Solution 11.3.2 — read before assign

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

Assigning step later in the function makes step local throughout, so the
print reads a local that has no value yet — UnboundLocalError. Read the
value through a parameter (or remove the local assignment) so the read
is valid.

Exercise: ex_11_3_2.py
"""

step = 1

def advance(step):
    print("Current:", step)
    step = step + 1

advance(step)
