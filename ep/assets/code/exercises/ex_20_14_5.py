"""Exercise 20.14.5 — Verifying a reading list

Chapter 20: Common Pitfalls — Everyday Programming

The program checks whether the books read so far match the planned
reading list.

This program contains exactly one bug. Solution: sol_20_14_5.py
"""

planned = ["Physics", "Algebra", "Biology"]
read_so_far = ["Physics", "Algebra", "Biology"]
if read_so_far is planned:
    print("You finished the planned books!")
else:
    print("Some planned books remain")
