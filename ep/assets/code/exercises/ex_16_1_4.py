"""Exercise 16.1.4 — Temperature reading

Chapter 16: Handling Failures — Everyday Programming

This program reads a Celsius temperature and converts it to Fahrenheit,
handling bad input.

This program contains exactly one bug. Solution: sol_16_1_4.py
"""

try:
    celsius = float(input("Temperature in Celsius? "))
    fahrenheit = celsius * 9 / 5 + 32
    print("That is", fahrenheit, "degrees Fahrenheit.")
except ValueError
    print("That was not a valid number.")
