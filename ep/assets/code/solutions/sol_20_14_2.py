"""Solution 20.14.2 — Matching a password phrase

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The built string is a different object from the stored literal, so is
returns False even though the text matches. Compare values with ==.

Exercise: ex_20_14_2.py
"""

stored_phrase = "open sesame"
typed_phrase = " ".join(["open", "sesame"])
if typed_phrase == stored_phrase:
    print("Access granted")
else:
    print("Access denied")
