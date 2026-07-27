"""Exercise 9.3.5 — Free shipping

Chapter 9: Control Flow — Everyday Programming

Free shipping applies when the cart total is at least 50 or the customer
is a member. A $30 order from a member should print Free shipping.

This program contains exactly one bug. Solution: sol_9_3_5.py
"""

total = 30
is_member = True

if total >= 50 and is_member:
    print("Free shipping")
else:
    print("Pay shipping")
# expected: Free shipping
