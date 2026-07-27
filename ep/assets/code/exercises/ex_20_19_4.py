"""Exercise 20.19.4 — Parsing a temperature

Chapter 20: Common Pitfalls — Everyday Programming

The program should convert typed text to a float and warn only on bad
number text.

This program contains exactly one bug. Solution: sol_20_19_4.py
"""

reading = "hot"
try:
    celsius = float(reading)
    print("Fahrenheit:", celsius * 9 / 5 + 32)
except:
    print("That is not a valid temperature")
