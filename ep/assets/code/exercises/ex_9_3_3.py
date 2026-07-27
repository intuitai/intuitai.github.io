"""Exercise 9.3.3 — Comfortable room

Chapter 9: Control Flow — Everyday Programming

A room is comfortable when the temperature is between 20 and 25 degrees
inclusive. At 30 degrees (too warm) this should print Adjust the
thermostat.

This program contains exactly one bug. Solution: sol_9_3_3.py
"""

temp_c = 30

if temp_c >= 20 or temp_c <= 25:
    print("Comfortable")
else:
    print("Adjust the thermostat")
# expected: Adjust the thermostat
