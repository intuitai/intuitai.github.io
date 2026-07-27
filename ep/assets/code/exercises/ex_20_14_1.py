"""Exercise 20.14.1 — Checking a student's full name

Chapter 20: Common Pitfalls — Everyday Programming

This program should announce a match when the typed name equals the
enrolled name.

This program contains exactly one bug. Solution: sol_20_14_1.py
"""

enrolled_name = "Ada Lovelace"
typed_name = " ".join(["Ada", "Lovelace"])
if typed_name is enrolled_name:
    print("Name matches our records")
else:
    print("Name does not match")
