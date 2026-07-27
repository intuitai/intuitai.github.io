"""Solution 5.5.3 — Checking for a value

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

The test is not None is False when the value is None, so the program
runs the wrong branch and prints "has value". Use is None so a None
value prints "missing".

Exercise: ex_5_5_3.py
"""

favorite = None

if favorite is None:
    print("missing")
else:
    print("has value")
# expected: missing
