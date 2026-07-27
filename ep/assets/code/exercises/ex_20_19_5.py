"""Exercise 20.19.5 — Reading a list position

Chapter 20: Common Pitfalls — Everyday Programming

This program should print the third score and warn only when the
position is out of range.

This program contains exactly one bug. Solution: sol_20_19_5.py
"""

scores = [88, 92]
try:
    print("Third score:", scores[2])
except:
    print("There is no score at that position")
