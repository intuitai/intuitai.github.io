"""Exercise 17.2.2 — Speed test

Chapter 17: Testing — Everyday Programming

This pytest function should verify that traveling 100 km in 2 hours
gives a speed of 50 km/h.

This program contains exactly one bug. Solution: sol_17_2_2.py
"""

def speed(distance, time):
    return distance * time

def test_speed():
    assert speed(100, 2) == 50
