"""Solution 20.1.1 — Missing colon after if

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

The if header is missing the trailing :, so Python cannot tell where the
condition ends and the block begins. Adding the colon fixes the parse
error.

Exercise: ex_20_1_1.py
"""

temperature = 39
if temperature >= 38:
    print("Fever")
