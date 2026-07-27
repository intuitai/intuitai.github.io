"""Exercise 20.24.2 — Final price after discount

Chapter 20: Common Pitfalls — Everyday Programming

The program should subtract a 20 percent discount from a $50 item and
print 40.0.

This program contains exactly one bug. Solution: sol_20_24_2.py
"""

def final_price(price, percent_off):
    discount = price * percent_off
    return price - discount

print("Final price:", final_price(50, 20))  # Final price: 40.0
