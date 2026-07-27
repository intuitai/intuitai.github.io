"""Exercise 10.5.1 — Calling by name

Chapter 10: Functions — Everyday Programming

This program should print "Lina is 12 years old" using keyword
arguments.

This program contains exactly one bug. Solution: sol_10_5_1.py
"""

def introduce(name, age):
    print(name, "is", age, "years old")

introduce(name="Lina", age=12, grade=7)
