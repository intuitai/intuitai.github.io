"""Solution 6.3.4 — Duck typing a method call

Chapter 6: Objects — Everyday Programming

Bug type: Logical

device.tick only looks up the method; it never calls it, so
watch.seconds stays 0. Adding parentheses — device.tick() — actually
advances each device.

Exercise: ex_6_3_4.py
"""

class Stopwatch:
    def __init__(self):
        self.seconds = 0

    def tick(self):
        self.seconds = self.seconds + 1

class Metronome:
    def __init__(self):
        self.beats = 0

    def tick(self):
        self.beats = self.beats + 1

def advance(devices):
    for device in devices:
        device.tick()

watch = Stopwatch()
advance([watch])
print(watch.seconds)   # 1
