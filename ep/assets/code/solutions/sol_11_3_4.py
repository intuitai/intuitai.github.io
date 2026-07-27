"""Solution 11.3.4 — local sum inside a loop

Chapter 11: Scoping — Everyday Programming

Bug type: Logical

The running total should add each distance, but the loop subtracts,
giving a negative total. Use addition.

Exercise: ex_11_3_4.py
"""

distance = 0
trips = [10, 15, 20]

def trip_total():
    distance = 0
    for d in trips:
        distance = distance + d
    return distance

print("Total distance:", trip_total())
