"""Solution 17.1.5 — Total cost with tax

Chapter 17: Testing — Everyday Programming

Bug type: Logical

The function is correct (20 + 2 = 22), but the expected value in the
assert is 20 instead of 22, so the check fails. The fix corrects the
expected value.

Exercise: ex_17_1_5.py
"""

def total_with_tax(price):
    return price + price * 0.10

assert total_with_tax(20) == 22
print("passed")
