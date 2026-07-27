"""Solution 7.5.3 — Missing value check

Chapter 7: Operators — Everyday Programming

Bug type: Logical

measurement is not None is False when the value really is None, the
opposite of what we want. Use the identity operator is to test that the
value is exactly None.

Exercise: ex_7_5_3.py
"""

measurement = None
is_missing = measurement is None
print(is_missing)   # True
