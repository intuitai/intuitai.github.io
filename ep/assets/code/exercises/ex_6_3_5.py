"""Exercise 6.3.5 — Trusting the interface

Chapter 6: Objects — Everyday Programming

Any sensor that provides a read() method can be sampled.

This program contains exactly one bug. Solution: sol_6_3_5.py
"""

class TempSensor:
    def read(self):
        return 21.5

class HumiditySensor:
    def read(self):
        return 48.0

def sample(sensor):
    return sensor.read

print(sample(TempSensor()))       # 21.5
print(sample(HumiditySensor()))   # 48.0
