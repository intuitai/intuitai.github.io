"""Solution 13.1.1 — Square root with math

Chapter 13: Modules — Everyday Programming

Bug type: Runtime

The Pythagorean theorem adds the squares of the legs, but this code
subtracts them, so math.sqrt receives 9-16=-7 and raises a ValueError
(math domain error). Change the - to +.

Exercise: ex_13_1_1.py
"""

import math

leg_a = 3
leg_b = 4
hypotenuse = math.sqrt(leg_a ** 2 + leg_b ** 2)
print(hypotenuse)   # 5.0
