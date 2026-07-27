"""Solution 10.7.3 — Printing is not returning

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The function prints but returns None, so area is None and area * 2
raises a TypeError. Return the value instead of printing it.

Exercise: ex_10_7_3.py
"""

def circle_area(radius):
    return 3.14 * radius * radius

area = circle_area(5)
print(area * 2)  # uses the area twice
