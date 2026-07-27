"""Exercise 17.2.5 — Doubling a recipe

Chapter 17: Testing — Everyday Programming

This pytest function should verify that doubling 3 cups of flour gives 6
cups.

This program contains exactly one bug. Solution: sol_17_2_5.py
"""

def double_recipe(cups):
    return cups * 2

def test_double_recipe():
    assert double_recipe(3) = 6
