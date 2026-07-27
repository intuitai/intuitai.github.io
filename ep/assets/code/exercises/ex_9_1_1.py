"""Exercise 9.1.1 — Grading with elif

Chapter 9: Control Flow — Everyday Programming

This program should print the letter grade for a score. A score of 82
should print Grade: B.

This program contains exactly one bug. Solution: sol_9_1_1.py
"""

score = 82

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else
    print("Needs improvement")
