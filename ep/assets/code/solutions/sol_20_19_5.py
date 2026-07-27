"""Solution 20.19.5 — Reading a list position

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The broad except: hides real bugs. An out-of-range index raises
IndexError, so catch exactly that.

Exercise: ex_20_19_5.py
"""

scores = [88, 92]
try:
    print("Third score:", scores[2])
except IndexError:
    print("There is no score at that position")
