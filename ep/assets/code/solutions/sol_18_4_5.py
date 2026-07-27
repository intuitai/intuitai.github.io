"""Solution 18.4.5 — Speed from distance and time

Chapter 18: Bugs — Everyday Programming

Bug type: Logical

Printing result reveals the division is inverted: speed is distance
divided by time, not time divided by distance. Swapping the operands
gives the correct speed.

Exercise: ex_18_4_5.py
"""

def speed(distance_km, time_hours):
    result = distance_km / time_hours
    return result

print(speed(150, 3))   # 50.0
