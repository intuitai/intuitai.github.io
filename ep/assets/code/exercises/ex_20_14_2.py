"""Exercise 20.14.2 — Matching a password phrase

Chapter 20: Common Pitfalls — Everyday Programming

The program should grant access when the typed phrase equals the stored
phrase.

This program contains exactly one bug. Solution: sol_20_14_2.py
"""

stored_phrase = "open sesame"
typed_phrase = " ".join(["open", "sesame"])
if typed_phrase is stored_phrase:
    print("Access granted")
else:
    print("Access denied")
