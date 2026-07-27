"""Exercise 10.5.4 — Keyword after positional

Chapter 10: Functions — Everyday Programming

This program should print "Sam scored 95" using one positional and one
keyword argument.

This program contains exactly one bug. Solution: sol_10_5_4.py
"""

def score_line(name, points):
    print(name, "scored", points)

score_line(name="Sam", 95)
