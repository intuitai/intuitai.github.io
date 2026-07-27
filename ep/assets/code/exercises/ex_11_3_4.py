"""Exercise 11.3.4 — local sum inside a loop

Chapter 11: Scoping — Everyday Programming

This program should add up the distances of three trips using a local
running total and print 45.

This program contains exactly one bug. Solution: sol_11_3_4.py
"""

distance = 0
trips = [10, 15, 20]

def trip_total():
    distance = 0
    for d in trips:
        distance = distance - d
    return distance

print("Total distance:", trip_total())
# Expected:
# Total distance: 45
