"""Solution 16.2.2 — Adding a measurement

Chapter 16: Handling Failures — Everyday Programming

Bug type: Runtime

Adding an integer to a string raises TypeError, but the code catches
ZeroDivisionError, so the error is not caught and the program crashes.
Catch TypeError.

Exercise: ex_16_2_2.py
"""

total = 100
new_value = "twelve"
try:
    total = total + new_value
except TypeError:
    print("That measurement was not a number.")
print("Total is", total)
