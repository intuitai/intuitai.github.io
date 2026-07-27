"""Exercise 6.1.5 — Method calls need parentheses

Chapter 6: Objects — Everyday Programming

This class stores a circle's radius and returns its circumference.

This program contains exactly one bug. Solution: sol_6_1_5.py
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius

wheel = Circle(10)
print(wheel.circumference)   # 62.8318
