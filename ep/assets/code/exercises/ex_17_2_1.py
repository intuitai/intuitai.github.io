"""Exercise 17.2.1 — Perimeter test

Chapter 17: Testing — Everyday Programming

This pytest function checks that the perimeter of a square with side 5
is 20.

This program contains exactly one bug. Solution: sol_17_2_1.py
"""

def square_perimeter(side):
    return 4 * side

def test_square_perimeter():
    assert square_perimeter(5) == 25
