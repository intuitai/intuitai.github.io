"""Solution 17.2.3 — Discount test

Chapter 17: Testing — Everyday Programming

Bug type: Logical

A pytest test should check with assert and not return a value; the
trailing return True makes the test look like it passes regardless.
Removing it leaves the assertion as the real check.

Exercise: ex_17_2_3.py
"""

def discounted_price(price, percent_off):
    return price - price * percent_off / 100

def test_discounted_price():
    assert discounted_price(50, 20) == 40
