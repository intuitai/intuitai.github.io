"""Solution 20.1.3 — Missing colon after while

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

The while header needs a colon before its block. Adding : lets the
countdown loop parse and run.

Exercise: ex_20_1_3.py
"""

seconds = 3
while seconds > 0:
    print(seconds)
    seconds = seconds - 1
