"""Solution 20.1.2 — Missing colon after for

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

A for loop header must end with :. Without it the program will not run;
adding the colon resolves it.

Exercise: ex_20_1_2.py
"""

distances = [58, 108, 150]
for distance in distances:
    print(distance)
