"""Solution 20.13.4 — Masking a letter

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Assigning to secret[3] fails because strings cannot be changed in place,
raising TypeError. Rebuild the string from its slices.

Exercise: ex_20_13_4.py
"""

secret = "open"
secret = secret[:3] + "*"
print(secret)
