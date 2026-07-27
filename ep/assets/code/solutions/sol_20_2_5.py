"""Solution 20.2.5 — Indentation mixing two blocks

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

The closing print is indented two spaces, matching neither the loop body
nor the top level, so Python raises an IndentationError. Dedenting it to
the top level fixes it.

Exercise: ex_20_2_5.py
"""

grades = [88, 91, 79]
for grade in grades:
    print(grade)
print("Report complete")
