"""Solution 9.3.5 — Free shipping

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

Free shipping should apply when *either* condition holds, but and
requires both, so a member with a $30 order is wrongly charged. Using or
matches the rule.

Exercise: ex_9_3_5.py
"""

total = 30
is_member = True

if total >= 50 or is_member:
    print("Free shipping")
else:
    print("Pay shipping")
# expected: Free shipping
