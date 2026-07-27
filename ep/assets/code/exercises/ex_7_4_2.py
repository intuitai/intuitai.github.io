"""Exercise 7.4.2 — Weekend or holiday

Chapter 7: Operators — Everyday Programming

You can sleep in if it is a weekend or a holiday. This program should
print True.

This program contains exactly one bug. Solution: sol_7_4_2.py
"""

is_weekend = False
is_holiday = True
sleep_in = is_weekend and is_holiday
print(sleep_in)   # expected: True
