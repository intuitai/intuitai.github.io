"""Exercise 17.3.2 — Floating-point area

Chapter 17: Testing — Everyday Programming

This test checks the area of a circle of radius 2 (about 12.566) and
should pass.

This program contains exactly one bug. Solution: sol_17_3_2.py
"""

import math

def area_circle(radius):
    return math.pi * radius ** 2

def test_area_circle():
    assert area_circle(2) == 12.566
