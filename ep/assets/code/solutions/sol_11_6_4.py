"""Solution 11.6.4 — a local inside a method

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

area() uses bare width, which is not defined in the method's local
scope, so Python raises NameError. Read the stored side through
self.width.

Exercise: ex_11_6_4.py
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        result = self.width * self.height
        return result

box = Rectangle(3, 4)
print("Area:", box.area())
