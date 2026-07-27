"""Exercise 6.2.4 — Instance overriding shared default

Chapter 6: Objects — Everyday Programming

Every thermostat shares a default target, but the kitchen is set warmer
for itself only. The bedroom should keep the shared default.

This program contains exactly one bug. Solution: sol_6_2_4.py
"""

class Thermostat:
    target_c = 20

    def __init__(self, room):
        self.room = room

kitchen = Thermostat("kitchen")
bedroom = Thermostat("bedroom")
Thermostat.target_c = 22

print(kitchen.target_c)   # 22
print(bedroom.target_c)   # 20
