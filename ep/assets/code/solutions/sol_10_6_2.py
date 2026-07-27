"""Solution 10.6.2 — Unpacking the result

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The pair is stored in one name quotient, and remainder is never defined,
so printing it raises a NameError. Unpack into two names.

Exercise: ex_10_6_2.py
"""

def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(17, 5)
print(quotient, remainder)  # 3 2
