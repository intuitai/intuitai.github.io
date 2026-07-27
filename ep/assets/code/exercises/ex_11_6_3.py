"""Exercise 11.6.3 — class variable shared by all

Chapter 11: Scoping — Everyday Programming

This program gives every Planet the same unit and should print "km" for
two planets.

This program contains exactly one bug. Solution: sol_11_6_3.py
"""

class Planet:
    unit = "km"

    def __init__(self, name):
        self.name = name

earth = Planet("Earth")
mars = Planet("Mars")
print(earth.unit)
print(mars.units)
# Expected:
# km
# km
