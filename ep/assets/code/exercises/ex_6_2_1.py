"""Exercise 6.2.1 — Instance vs class attribute

Chapter 6: Objects — Everyday Programming

Every planet shares the same gravity unit, but each has its own mass.
This program should print each planet's name and the shared unit.

This program contains exactly one bug. Solution: sol_6_2_1.py
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
print(earth.unit)                       # m/s^2
