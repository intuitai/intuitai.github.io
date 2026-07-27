"""Exercise 10.7.3 — Printing is not returning

Chapter 10: Functions — Everyday Programming

This should store the area of a circle approximation and print about
78.5, then use it again.

This program contains exactly one bug. Solution: sol_10_7_3.py
"""

def circle_area(radius):
    print(3.14 * radius * radius)

area = circle_area(5)
print(area * 2)  # uses the area twice
