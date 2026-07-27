"""Solution 6.2.1 — Instance vs class attribute

Chapter 6: Objects — Everyday Programming

Bug type: Runtime

The class attribute is named gravity_unit, but the last line reads
earth.unit, which does not exist. Using earth.gravity_unit fixes the
AttributeError.

Exercise: ex_6_2_1.py
"""

class Planet:
    gravity_unit = "m/s^2"

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

earth = Planet("Earth", 5.97e24)
mars = Planet("Mars", 6.42e23)

print(earth.name, earth.gravity_unit)   # Earth m/s^2
print(mars.name, mars.gravity_unit)     # Mars m/s^2
print(earth.gravity_unit)               # m/s^2
