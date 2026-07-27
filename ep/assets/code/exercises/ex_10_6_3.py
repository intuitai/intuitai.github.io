"""Exercise 10.6.3 — Matching the count

Chapter 10: Functions — Everyday Programming

This program should unpack a name and an age into two variables.

This program contains exactly one bug. Solution: sol_10_6_3.py
"""

def person():
    return "Luis", 14, "grade 8"

name, age = person()
print(name, age)  # Luis 14
