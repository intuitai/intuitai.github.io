"""Solution 9.1.4 — Pass or fail

Chapter 9: Control Flow — Everyday Programming

Bug type: Syntax

The else is indented as if it were inside the if body, which is illegal.
Aligning else with if fixes it.

Exercise: ex_9_1_4.py
"""

score = 75

if score >= 60:
    print("Pass")
else:
    print("Fail")
