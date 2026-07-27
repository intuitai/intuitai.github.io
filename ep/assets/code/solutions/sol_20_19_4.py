"""Solution 20.19.4 — Parsing a temperature

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

A bare except: masks unrelated problems. float() raises ValueError on
non-numeric text, so catch ValueError.

Exercise: ex_20_19_4.py
"""

reading = "hot"
try:
    celsius = float(reading)
    print("Fahrenheit:", celsius * 9 / 5 + 32)
except ValueError:
    print("That is not a valid temperature")
