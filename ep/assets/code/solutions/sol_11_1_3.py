"""Solution 11.1.3 — a global constant for area

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

The global pi is visible inside the function, but area is created
*inside* circle_area, so it does not exist at the top level and the
final print raises NameError. Return the value and capture it in a
variable.

Exercise: ex_11_1_3.py
"""

pi = 3.14159

def circle_area():
    return pi * 3 * 3

area = circle_area()
print("Area:", area)   # Area: 28.27431
