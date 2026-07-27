"""Exercise 17.3.5 — Approximate division

Chapter 17: Testing — Everyday Programming

This pytest function uses pytest.approx to check that dividing 1 by 3 is
about 0.3333.

This program contains exactly one bug. Solution: sol_17_3_5.py
"""

import pytest

def divide(a, b):
    return a / b

def test_divide():
    assert divide(1, 3) == pytest.approx(0.3333, abs=0)
