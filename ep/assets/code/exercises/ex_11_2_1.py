"""Exercise 11.2.1 — local hides global, on purpose

Chapter 11: Scoping — Everyday Programming

The global discount is 0.10. Inside checkout() a local discount of 0.25
should be used for one sale, but the global should stay 0.10. The
program should print the local rate then the global rate.

This program contains exactly one bug. Solution: sol_11_2_1.py
"""

discount = 0.10

def checkout():
    discount = 0.25
    print("Sale rate:", discount)

checkout()
print("Normal rate:", discount)
# Expected:
# Sale rate: 0.1
# Normal rate: 0.1
