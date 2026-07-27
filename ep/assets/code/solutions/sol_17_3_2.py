"""Solution 17.3.2 — Floating-point area

Chapter 17: Testing — Everyday Programming

Bug type: Logical

Comparing a floating-point result with plain == fails here because
area_circle(2) is 12.566370…, not exactly 12.566. Wrap the expected
value in pytest.approx to allow a tiny tolerance.

Exercise: ex_17_3_2.py
"""

import math
import pytest

def area_circle(radius):
    return math.pi * radius ** 2

def test_area_circle():
    assert area_circle(2) == pytest.approx(12.566, abs=1e-3)
