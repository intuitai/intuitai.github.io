"""Exercise 20.20.5 — Confirming a unit

Chapter 20: Common Pitfalls — Everyday Programming

This program should accept the unit "kg" whether typed as "KG", "Kg", or
"kg".

This program contains exactly one bug. Solution: sol_20_20_5.py
"""

unit = "KG"
if unit.upper() == "kg":
    print("Kilograms")
