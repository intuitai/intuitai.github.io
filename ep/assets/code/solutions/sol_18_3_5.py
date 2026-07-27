"""Solution 18.3.5 — Fahrenheit to Celsius

Chapter 18: Bugs — Everyday Programming

Bug type: Logical

The conversion factor is inverted: Fahrenheit to Celsius multiplies by 5
/ 9, not 9 / 5. Swapping the fraction gives the right temperature.

Exercise: ex_18_3_5.py
"""

def f_to_c(f):
    return (f - 32) * 5 / 9

print(f_to_c(212))   # 100.0
