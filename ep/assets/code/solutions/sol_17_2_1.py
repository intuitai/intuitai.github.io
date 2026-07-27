"""Solution 17.2.1 — Perimeter test

Chapter 17: Testing — Everyday Programming

Bug type: Logical

The function correctly returns 4 × 5 = 20, but the test asserts 25, so
it fails. The fix corrects the expected value to 20.

Exercise: ex_17_2_1.py
"""

def square_perimeter(side):
    return 4 * side

def test_square_perimeter():
    assert square_perimeter(5) == 20
