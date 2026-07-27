"""Solution 16.1.1 — Reading an age

Chapter 16: Handling Failures — Everyday Programming

Bug type: Runtime

The int(raw) call happens *outside* the try, so a non-numeric entry
raises ValueError before the except can catch it and the program
crashes. Move the conversion inside the try so the failing line is
actually protected.

Exercise: ex_16_1_1.py
"""

while True:
    raw = input("Enter your age in years: ")
    try:
        age = int(raw)
        print("Your age is", age)
        break
    except ValueError:
        print("That was not a whole number. Try again.")
