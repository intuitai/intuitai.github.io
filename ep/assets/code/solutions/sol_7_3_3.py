"""Solution 7.3.3 — Temperature in safe range

Chapter 7: Operators — Everyday Programming

Bug type: Logical

The chained comparison 0 < temp_c > 100 checks that the temperature is
above both 0 and 100, which is wrong. It should be 0 < temp_c < 100 to
test the range between them.

Exercise: ex_7_3_3.py
"""

temp_c = 25
in_range = 0 < temp_c < 100
print(in_range)   # True
