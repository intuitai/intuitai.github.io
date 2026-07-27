"""Exercise 16.2.3 — Average speed

Chapter 16: Handling Failures — Everyday Programming

This program reads a distance and a time, divides to get average speed,
and should report a typed-in non-number and a zero time with separate
messages.

This program contains exactly one bug. Solution: sol_16_2_3.py
"""

distance = float(input("Distance in meters? "))
time = float(input("Time in seconds? "))
try:
    speed = distance / time
    print("Average speed:", speed)
except Exception:
    print("Distance was not a number.")
except ZeroDivisionError:
    print("Time cannot be zero.")
