"""Solution 13.2.5 — Kelvin conversion formula

Chapter 13: Modules — Everyday Programming

Bug type: Logical

The Celsius-to-Kelvin formula adds 273.15, but the function subtracts
it, giving -273.15 instead of 273.15. Change the operator to +.

Exercise: ex_13_2_5.py
"""

# file: conversions.py
def c_to_k(celsius):
    return celsius + 273.15

# file: main.py
from conversions import c_to_k

print(c_to_k(0))   # 273.15
