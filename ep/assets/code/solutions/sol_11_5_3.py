"""Solution 11.5.3 — nonlocal keyword

Chapter 11: Scoping — Everyday Programming

Bug type: Syntax

The final print call is missing its closing parenthesis, so the file
will not parse. Add the closing parenthesis.

Exercise: ex_11_5_3.py
"""

def make_tracker():
    highest = 0

    def record(value):
        nonlocal highest
        if value > highest:
            highest = value
        return highest

    return record

record = make_tracker()
record(4)
print("Highest:", record(9))
