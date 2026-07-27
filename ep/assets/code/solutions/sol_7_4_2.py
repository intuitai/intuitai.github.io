"""Solution 7.4.2 — Weekend or holiday

Chapter 7: Operators — Everyday Programming

Bug type: Logical

Either condition should let you sleep in, but and requires both to be
true, giving False. Use or.

Exercise: ex_7_4_2.py
"""

is_weekend = False
is_holiday = True
sleep_in = is_weekend or is_holiday
print(sleep_in)   # True
