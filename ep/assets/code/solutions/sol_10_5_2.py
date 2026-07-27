"""Solution 10.5.2 — Order independence

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The keyword values are swapped: time=100 and distance=5 give 0.05, not
20.0. Match each keyword to the intended value.

Exercise: ex_10_5_2.py
"""

def speed(distance, time):
    return distance / time

print(speed(distance=100, time=5))  # 20.0
