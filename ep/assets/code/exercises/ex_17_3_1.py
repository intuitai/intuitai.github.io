"""Exercise 17.3.1 — Sum of an empty list

Chapter 17: Testing — Everyday Programming

This pytest function tests the edge case of summing an empty list, which
should give 0.

This program contains exactly one bug. Solution: sol_17_3_1.py
"""

def total(numbers):
    running = 0
    for n in numbers:
        running += n
    return running

def test_total_empty():
    assert total([]) == 1
