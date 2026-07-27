"""Solution 17.1.4 — Percent of a total

Chapter 17: Testing — Everyday Programming

Bug type: Syntax

The function header is missing the colon at the end of the def line, so
the file will not parse. Adding the colon fixes it.

Exercise: ex_17_1_4.py
"""

def percent(part, whole):
    return part / whole * 100

assert percent(25, 50) == 50
print("passed")
