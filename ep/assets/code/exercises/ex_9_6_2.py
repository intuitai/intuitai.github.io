"""Exercise 9.6.2 — Countdown

Chapter 9: Control Flow — Everyday Programming

This program should count down from 3 to 1 and then print Liftoff.

This program contains exactly one bug. Solution: sol_9_6_2.py
"""

count = 3

while count > 0:
    print(count)
    count += 1

print("Liftoff")
# Expected: 3 2 1 then Liftoff
