"""Solution 17.2.5 — Doubling a recipe

Chapter 17: Testing — Everyday Programming

Bug type: Syntax

The assert uses a single = (assignment) instead of == (comparison),
which is a syntax error. Using == fixes the comparison.

Exercise: ex_17_2_5.py
"""

def double_recipe(cups):
    return cups * 2

def test_double_recipe():
    assert double_recipe(3) == 6
