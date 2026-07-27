"""Exercise 7.4.5 — Free shipping

Chapter 7: Operators — Everyday Programming

Shipping is free if the order is over $50 or the customer is a member.
This program should print True for a $30 order by a member.

This program contains exactly one bug. Solution: sol_7_4_5.py
"""

order_total = 30
is_member = True
free_shipping = order_total > 50 and is_member
print(free_shipping)   # expected: True
