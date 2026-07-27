"""Solution 17.2.2 — Speed test

Chapter 17: Testing — Everyday Programming

Bug type: Logical

Speed is distance divided by time, but the function multiplies them,
returning 200 instead of 50. Changing * to / fixes the formula.

Exercise: ex_17_2_2.py
"""

def speed(distance, time):
    return distance / time

def test_speed():
    assert speed(100, 2) == 50
