"""Solution 18.2.1 — Average speed

Chapter 18: Bugs — Everyday Programming

Bug type: Runtime

Calling the function with hours = 0 divides by zero at run time, raising
ZeroDivisionError. Guarding against a zero time (or passing a real
duration) avoids the crash.

Exercise: ex_18_2_1.py
"""

def average_speed(distance, hours):
    if hours == 0:
        return "Time cannot be zero"
    return distance / hours

print(average_speed(120, 2))   # 60.0
