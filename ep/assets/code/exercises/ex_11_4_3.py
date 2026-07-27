"""Exercise 11.4.3 — global keyword spelling

Chapter 11: Scoping — Everyday Programming

This program should use the global keyword so the function changes the
module-level temperature to 25, and print 25.

This program contains exactly one bug. Solution: sol_11_4_3.py
"""

temperature = 0

def set_room():
    Global temperature
    temperature = 25

set_room()
print("Temperature:", temperature)
# Expected:
# Temperature: 25
