"""Exercise 16.1.1 — Reading an age

Chapter 16: Handling Failures — Everyday Programming

This program should keep asking until the user types a whole number for
their age, then print it.

This program contains exactly one bug. Solution: sol_16_1_1.py
"""

while True:
    raw = input("Enter your age in years: ")
    age = int(raw)
    try:
        print("Your age is", age)
        break
    except ValueError:
        print("That was not a whole number. Try again.")
