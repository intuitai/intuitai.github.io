"""Solution 20.17.4 — Accumulating distance

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Assigning distance_km inside drive makes it local, so the read raises
UnboundLocalError. Add global distance_km.

Exercise: ex_20_17_4.py
"""

distance_km = 0

def drive(leg):
    global distance_km
    distance_km = distance_km + leg

drive(45)
print("Distance:", distance_km)
