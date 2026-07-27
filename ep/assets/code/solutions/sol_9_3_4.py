"""Solution 9.3.4 — Out of stock

Chapter 9: Control Flow — Everyday Programming

Bug type: Syntax

not in_stock = True mixes not with an assignment, which is invalid. The
intent is simply to test the negation, so write if not in_stock:.

Exercise: ex_9_3_4.py
"""

in_stock = False

if not in_stock:
    print("Reorder")
