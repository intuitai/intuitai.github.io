"""Solution 20.14.1 — Checking a student's full name

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The name built with join is a brand-new string object, so is (which
tests identity) returns False even though the text matches. Compare
values with ==.

Exercise: ex_20_14_1.py
"""

enrolled_name = "Ada Lovelace"
typed_name = " ".join(["Ada", "Lovelace"])
if typed_name == enrolled_name:
    print("Name matches our records")
else:
    print("Name does not match")
