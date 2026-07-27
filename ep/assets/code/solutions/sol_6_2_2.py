"""Solution 6.2.2 — Shared mutable class attribute

Chapter 6: Objects — Everyday Programming

Bug type: Logical

laps is a class attribute, so a single list is shared by every runner;
amir.record and beth.record append to the same list. Each runner needs
its own list, created as an instance attribute in __init__.

Exercise: ex_6_2_2.py
"""

class Runner:
    def __init__(self, name):
        self.name = name
        self.laps = []

    def record(self, seconds):
        self.laps.append(seconds)

amir = Runner("Amir")
beth = Runner("Beth")
amir.record(58)
beth.record(61)
print(amir.laps)   # [58]
print(beth.laps)   # [61]
