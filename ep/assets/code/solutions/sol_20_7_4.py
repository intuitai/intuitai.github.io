"""Solution 20.7.4 — Comparing typed age to a limit

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

age is a string, so age >= 18 compares a string with an int and raises
TypeError. Convert the input to int before comparing.

Exercise: ex_20_7_4.py
"""

age = int(input("Your age: "))
if age >= 18:
    print("Adult")
