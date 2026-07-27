"""Solution 20.14.5 — Verifying a reading list

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

Two lists with identical contents are still different objects, so is is
always False here. Use == to compare contents.

Exercise: ex_20_14_5.py
"""

planned = ["Physics", "Algebra", "Biology"]
read_so_far = ["Physics", "Algebra", "Biology"]
if read_so_far == planned:
    print("You finished the planned books!")
else:
    print("Some planned books remain")
