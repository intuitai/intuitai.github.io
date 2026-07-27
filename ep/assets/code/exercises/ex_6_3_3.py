"""Exercise 6.3.3 — Behavior over type

Chapter 6: Objects — Everyday Programming

A function should work with anything that has a length attribute.

This program contains exactly one bug. Solution: sol_6_3_3.py
"""

class Field:
    def __init__(self, length):
        self.length = length

class Pool:
    def __init__(self, length):
        self.length = length

def meters_of(thing):
    return thing.size

print(meters_of(Field(100)))   # 100
print(meters_of(Pool(25)))     # 25
