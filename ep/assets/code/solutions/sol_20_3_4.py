"""Solution 20.3.4 — Assignment inside a while

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

A while condition cannot use =; it needs a comparison. The intended loop
continues while the count is below 50, so use <.

Exercise: ex_20_3_4.py
"""

count = 5
while count < 50:
    count = count * 2
    print(count)
