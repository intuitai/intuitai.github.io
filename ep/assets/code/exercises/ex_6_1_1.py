"""Exercise 6.1.1 — Defining a class

Chapter 6: Objects — Everyday Programming

This class should store a rectangle's width and height and report its
area.

This program contains exactly one bug. Solution: sol_6_1_1.py
"""

class Rectangle:
    def __init__(self, width, height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

room = Rectangle(4, 3)
print(room.area())   # 12
