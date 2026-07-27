"""Solution 20.3.1 — Assignment inside an if

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Syntax

= assigns and cannot appear as a condition; comparing requires ==. Using
== makes the test valid.

Exercise: ex_20_3_1.py
"""

thermostat = 20
if thermostat == 20:
    print("Comfortable")
