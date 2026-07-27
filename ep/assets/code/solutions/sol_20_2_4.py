"""Solution 20.2.4 — Over-indented statement

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

The second print is indented inconsistently relative to the if block,
causing an IndentationError. Matching the block's indentation (here,
dedenting it to the top level) fixes it.

Exercise: ex_20_2_4.py
"""

temperature = 100
if temperature >= 100:
    print("Boiling")
print("Done checking")
