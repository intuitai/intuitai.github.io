"""Solution 20.7.5 — Averaging a typed temperature

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

temperature is text, so temperature / 2 raises TypeError. Convert the
input to a number first (float allows decimals).

Exercise: ex_20_7_5.py
"""

temperature = float(input("Temperature: "))
print(temperature / 2)
