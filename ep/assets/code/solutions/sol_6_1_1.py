"""Solution 6.1.1 — Defining a class

Chapter 6: Objects — Everyday Programming

Bug type: Syntax

The def __init__(self, width, height) header is missing the colon at the
end, so Python cannot parse the method definition. Adding the colon
fixes it.

Exercise: ex_6_1_1.py
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

room = Rectangle(4, 3)
print(room.area())   # 12
