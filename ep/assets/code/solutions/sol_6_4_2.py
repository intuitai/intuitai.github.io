"""Solution 6.4.2 — Aliasing a list

Chapter 6: Objects — Everyday Programming

Bug type: Logical

list(readings) builds a brand-new list, so same_readings is a separate
object and appending to it does not change readings. To make both names
refer to the same list, assign directly with same_readings = readings.

Exercise: ex_6_4_2.py
"""

readings = [12, 15, 9]
same_readings = readings
same_readings.append(20)
print(readings)   # [12, 15, 9, 20]
