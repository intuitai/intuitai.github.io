"""Solution 6.1.2 — Using self

Chapter 6: Objects — Everyday Programming

Bug type: Runtime

Inside to_fahrenheit the bare name celsius is not defined; the value is
stored on the instance, so it must be reached through self“.celsius.
Using self.celsius fixes the NameError.

Exercise: ex_6_1_2.py
"""

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

reading = Temperature(100)
print(reading.to_fahrenheit())   # 212.0
