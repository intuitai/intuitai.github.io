"""Solution 20.20.5 — Confirming a unit

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

unit.upper() produces "KG", which never equals lowercase "kg". Compare
against the same case you converted to, for example .lower() == "kg".

Exercise: ex_20_20_5.py
"""

unit = "KG"
if unit.lower() == "kg":
    print("Kilograms")
