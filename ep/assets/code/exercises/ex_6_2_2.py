"""Exercise 6.2.2 — Shared mutable class attribute

Chapter 6: Objects — Everyday Programming

Each runner should keep a private list of lap times, but every runner
ends up sharing one list.

This program contains exactly one bug. Solution: sol_6_2_2.py
"""

class Runner:
    laps = []

    def __init__(self, name):
        self.name = name

    def record(self, seconds):
        self.laps.append(seconds)

amir = Runner("Amir")
beth = Runner("Beth")
amir.record(58)
beth.record(61)
print(amir.laps)   # [58]
print(beth.laps)   # [61]
