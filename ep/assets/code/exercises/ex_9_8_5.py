"""Exercise 9.8.5 — Skip a specific student

Chapter 9: Control Flow — Everyday Programming

This program should print every name except "Leo".

This program contains exactly one bug. Solution: sol_9_8_5.py
"""

names = ["Ana", "Leo", "Sam"]

for name in names:
    if name != "Leo":
        continue
    print(name)
# Expected: Ana Sam
