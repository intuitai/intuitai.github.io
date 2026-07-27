"""Solution 13.1.5 — Rounding a price up

Chapter 13: Modules — Everyday Programming

Bug type: Runtime

With from math import ceil, the name brought into scope is ceil, not
math, so math.ceil(price) raises NameError. Call ceil(price) directly.

Exercise: ex_13_1_5.py
"""

from math import ceil

price = 4.20
rounded_up = ceil(price)
print(rounded_up)   # 5
