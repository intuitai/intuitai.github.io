"""Exercise 11.6.4 — a local inside a method

Chapter 11: Scoping — Everyday Programming

This program computes a rectangle's area inside a method from stored
sides and should print 12.

This program contains exactly one bug. Solution: sol_11_6_4.py
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        result = width * self.height
        return result

box = Rectangle(3, 4)
print("Area:", box.area())
# Expected:
# Area: 12
