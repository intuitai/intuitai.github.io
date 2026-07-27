"""Exercise 16.1.5 — Validating a test score

Chapter 16: Handling Failures — Everyday Programming

This program should accept a score the user types only if it is a whole
number, then print it.

This program contains exactly one bug. Solution: sol_16_1_5.py
"""

raw = input("Enter your test score: ")
try:
    score = int(raw)
except ValueError:
    score = raw
print("Your score is", score)
