"""Solution 11.6.1 — self attribute vs local

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

In __init__, temperature = temperature just reassigns the local
parameter; it never stores anything on the object, so read() raises an
AttributeError for the missing self.temperature. Assign to
self.temperature.

Exercise: ex_11_6_1.py
"""

class Thermometer:
    def __init__(self, temperature):
        self.temperature = temperature

    def read(self):
        return self.temperature

device = Thermometer(22)
print("Temp:", device.read())
