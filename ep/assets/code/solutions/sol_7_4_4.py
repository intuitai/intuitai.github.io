"""Solution 7.4.4 — Safe to swim

Chapter 7: Operators — Everyday Programming

Bug type: Syntax

A boolean expression assigned to a variable must not end with a colon;
the trailing : makes the line invalid. Remove it.

Exercise: ex_7_4_4.py
"""

lifeguard_on_duty = True
water_is_calm = True
safe_to_swim = lifeguard_on_duty and water_is_calm
print(safe_to_swim)   # True
