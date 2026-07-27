"""Exercise 17.3.4 — Parametrized squares

Chapter 17: Testing — Everyday Programming

This parametrized pytest checks that squaring 0, 2, and 5 gives 0, 4,
and 25.

This program contains exactly one bug. Solution: sol_17_3_4.py
"""

import pytest

def square(n):
    return n ** 2

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (2, 4),
    (5, 20),
])
def test_square(n, expected):
    assert square(n) == expected
