"""Exercise 17.3.3 — Absolute value of negatives

Chapter 17: Testing — Everyday Programming

This pytest function tests the edge case of a negative input, expecting
abs_value(-7) to be 7.

This program contains exactly one bug. Solution: sol_17_3_3.py
"""

def abs_value(number):
    if number < 0:
        return number
    return number

def test_abs_value_negative():
    assert abs_value(-7) == 7
