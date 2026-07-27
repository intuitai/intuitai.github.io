"""Solution 9.1.1 — Grading with elif

Chapter 9: Control Flow — Everyday Programming

Bug type: Syntax

The else line is missing its colon, so Python cannot parse the block.
Adding the colon fixes it.

Exercise: ex_9_1_1.py
"""

score = 82

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Needs improvement")
