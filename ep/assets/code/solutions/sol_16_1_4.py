"""Solution 16.1.4 — Temperature reading

Chapter 16: Handling Failures — Everyday Programming

Bug type: Syntax

The except ValueError line is missing its colon, so the file will not
parse. Add the colon.

Exercise: ex_16_1_4.py
"""

try:
    celsius = float(input("Temperature in Celsius? "))
    fahrenheit = celsius * 9 / 5 + 32
    print("That is", fahrenheit, "degrees Fahrenheit.")
except ValueError:
    print("That was not a valid number.")
