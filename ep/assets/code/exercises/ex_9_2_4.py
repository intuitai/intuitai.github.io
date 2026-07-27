"""Exercise 9.2.4 — Speed limit check

Chapter 9: Control Flow — Everyday Programming

A car at exactly the speed limit is allowed. This program should print
OK when speed is at most 60. At 60 it should print OK.

This program contains exactly one bug. Solution: sol_9_2_4.py
"""

speed = 60
limit = 60

if speed < limit:
    print("OK")
else:
    print("Too fast")
# Expected: OK
