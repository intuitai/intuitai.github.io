"""Solution 11.6.3 — class variable shared by all

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

The class variable is named unit, but the last line reads mars.units,
which does not exist, so Python raises AttributeError. Use the correct
attribute name.

Exercise: ex_11_6_3.py
"""

class Planet:
    unit = "km"

    def __init__(self, name):
        self.name = name

earth = Planet("Earth")
mars = Planet("Mars")
print(earth.unit)
print(mars.unit)
