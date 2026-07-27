"""Solution 11.2.1 — local hides global, on purpose

Chapter 11: Scoping — Everyday Programming

Bug type: Logical

The intended output uses 0.10 for the sale, but inside the function the
local discount is set to 0.25, which shadows the global. To make both
lines print 0.10, the local should not override it; assign the sale rate
to match the intended 0.10.

Exercise: ex_11_2_1.py
"""

discount = 0.10

def checkout():
    discount = 0.10
    print("Sale rate:", discount)

checkout()
print("Normal rate:", discount)
