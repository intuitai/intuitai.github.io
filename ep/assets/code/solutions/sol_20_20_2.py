"""Solution 20.20.2 — Matching a chosen color

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

favorite.upper() gives "BLUE", which never equals the lowercase "blue".
Normalize both sides to the same case, for example .lower() == "blue".

Exercise: ex_20_20_2.py
"""

favorite = "Blue"
if favorite.lower() == "blue":
    print("You picked blue")
