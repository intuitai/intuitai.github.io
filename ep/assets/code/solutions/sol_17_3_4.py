"""Solution 17.3.4 — Parametrized squares

Chapter 17: Testing — Everyday Programming

Bug type: Logical

The third parameter case expects 20, but 5² = 25, so that case fails.
Correcting the expected value to 25 makes all parametrized cases pass.

Exercise: ex_17_3_4.py
"""

import pytest

def square(n):
    return n ** 2

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (2, 4),
    (5, 25),
])
def test_square(n, expected):
    assert square(n) == expected
