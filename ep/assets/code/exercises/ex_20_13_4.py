"""Exercise 20.13.4 — Masking a letter

Chapter 20: Common Pitfalls — Everyday Programming

This program should hide the last letter of a word with an asterisk.

This program contains exactly one bug. Solution: sol_20_13_4.py
"""

secret = "open"
secret[3] = "*"
print(secret)
