"""Exercise 20.19.1 — Converting a typed age

Chapter 20: Common Pitfalls — Everyday Programming

This program should turn typed text into a number and warn only when the
text is not a number.

This program contains exactly one bug. Solution: sol_20_19_1.py
"""

text = "12y"
try:
    age = int(text)
    print("Next year you will be", age + 1)
except:
    print("Please type a whole number")
