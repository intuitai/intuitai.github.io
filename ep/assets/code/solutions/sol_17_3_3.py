"""Solution 17.3.3 — Absolute value of negatives

Chapter 17: Testing — Everyday Programming

Bug type: Logical

For a negative input the function returns the number unchanged instead
of negating it, so abs_value(-7) gives -7. Returning -number in the
negative branch fixes the edge case.

Exercise: ex_17_3_3.py
"""

def abs_value(number):
    if number < 0:
        return -number
    return number

def test_abs_value_negative():
    assert abs_value(-7) == 7
