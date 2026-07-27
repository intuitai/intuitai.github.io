"""Solution 20.2.1 — Body not indented

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

The print after the if must be indented to form the block. Indenting it
by four spaces fixes the IndentationError.

Exercise: ex_20_2_1.py
"""

member = "Alex"
if member == "Alex":
    print("Welcome back")
