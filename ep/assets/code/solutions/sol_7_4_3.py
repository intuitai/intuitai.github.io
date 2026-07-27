"""Solution 7.4.3 — Not raining

Chapter 7: Operators — Everyday Programming

Bug type: Syntax

not is a prefix operator and must come before its value; writing
is_raining not will not parse. Move not in front to get not is_raining.

Exercise: ex_7_4_3.py
"""

is_raining = False
stay_dry = not is_raining
print(stay_dry)   # True
