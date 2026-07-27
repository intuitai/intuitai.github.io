"""Solution 20.20.3 — Checking a chemical symbol

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

"NA" == "Na" is False because the cases differ. Normalize the typed
symbol, for example with .capitalize().

Exercise: ex_20_20_3.py
"""

symbol = "NA"
if symbol.capitalize() == "Na":
    print("That is sodium")
