"""Solution 7.3.4 — Different answers

Chapter 7: Operators — Everyday Programming

Bug type: Syntax

The "not equal" operator is written !=, not = !, so the expression will
not parse. Use !=.

Exercise: ex_7_3_4.py
"""

correct_answer = 42
student_answer = 38
print(student_answer != correct_answer)   # True
