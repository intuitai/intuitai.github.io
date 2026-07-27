"""Solution 6.3.3 — Behavior over type

Chapter 6: Objects — Everyday Programming

Bug type: Runtime

Both objects expose a length attribute, but meters_of reads thing.size,
which neither class has. Reading thing.length fixes the AttributeError,
and any object with a length works.

Exercise: ex_6_3_3.py
"""

class Field:
    def __init__(self, length):
        self.length = length

class Pool:
    def __init__(self, length):
        self.length = length

def meters_of(thing):
    return thing.length

print(meters_of(Field(100)))   # 100
print(meters_of(Pool(25)))     # 25
