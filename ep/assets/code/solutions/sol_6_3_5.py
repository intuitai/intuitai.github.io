"""Solution 6.3.5 — Trusting the interface

Chapter 6: Objects — Everyday Programming

Bug type: Logical

sensor.read returns the bound method instead of the reading, so the
printout is a method reference, not a number. Calling sensor.read()
returns the value from whichever sensor was passed.

Exercise: ex_6_3_5.py
"""

class TempSensor:
    def read(self):
        return 21.5

class HumiditySensor:
    def read(self):
        return 48.0

def sample(sensor):
    return sensor.read()

print(sample(TempSensor()))       # 21.5
print(sample(HumiditySensor()))   # 48.0
