"""Solution 18.1.3 — Passing grade

Chapter 18: Bugs — Everyday Programming

Bug type: Syntax

The condition uses = (assignment) where a comparison == is required,
which is a syntax error inside an if. Using >= expresses the intended
“score is at least 60” test.

Exercise: ex_18_1_3.py
"""

score = 72
if score >= 60:
    print("Pass")
else:
    print("Fail")
