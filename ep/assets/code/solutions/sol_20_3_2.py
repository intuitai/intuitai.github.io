"""Solution 20.3.2 — Assignment when comparing a password length

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

A condition must compare with ==, not assign with =. Switching to ==
fixes the error.

Exercise: ex_20_3_2.py
"""

length = 8
if length == 8:
    print("Valid length")
