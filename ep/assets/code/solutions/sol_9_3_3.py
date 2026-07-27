"""Solution 9.3.3 — Comfortable room

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

With or, almost every temperature satisfies at least one side, so even
30 degrees prints “Comfortable”. The range requires *both* bounds, so
use and.

Exercise: ex_9_3_3.py
"""

temp_c = 30

if temp_c >= 20 and temp_c <= 25:
    print("Comfortable")
else:
    print("Adjust the thermostat")
# expected: Adjust the thermostat
