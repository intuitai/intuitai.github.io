"""Solution 11.1.1 — reading a global from a function

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

The top-level print reads speed_limit, but the global is named
speed_limit_kmh, so Python raises NameError. Use the correct global
name.

Exercise: ex_11_1_1.py
"""

speed_limit_kmh = 100

def report():
    print("Inside:", speed_limit_kmh)

report()
print("Outside:", speed_limit_kmh)
