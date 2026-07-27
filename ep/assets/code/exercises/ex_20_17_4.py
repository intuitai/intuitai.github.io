"""Exercise 20.17.4 — Accumulating distance

Chapter 20: Common Pitfalls — Everyday Programming

This program should add a new leg of a trip to the total distance
traveled.

This program contains exactly one bug. Solution: sol_20_17_4.py
"""

distance_km = 0

def drive(leg):
    distance_km = distance_km + leg

drive(45)
print("Distance:", distance_km)
