"""Solution 20.24.1 — Average speed of a trip

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The formula is reversed: speed is distance divided by time, not time
divided by distance. Swap the operands.

Exercise: ex_20_24_1.py
"""

def average_speed(distance, time):
    return distance / time

print("Average speed:", average_speed(150, 3))  # Average speed: 50.0
