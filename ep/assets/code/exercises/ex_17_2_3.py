"""Exercise 17.2.3 — Discount test

Chapter 17: Testing — Everyday Programming

This pytest function should check that a 20% discount on a $50 item
leaves a $40 price.

This program contains exactly one bug. Solution: sol_17_2_3.py
"""

def discounted_price(price, percent_off):
    return price - price * percent_off / 100

def test_discounted_price():
    assert discounted_price(50, 20) == 40
    return True
