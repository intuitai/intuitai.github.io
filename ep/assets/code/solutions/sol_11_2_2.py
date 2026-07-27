"""Solution 11.2.2 — the local shadow should win inside

Chapter 11: Scoping — Everyday Programming

Bug type: Logical

To convert kilometers to meters you multiply by 1000; the code divides
instead, so it shrinks the value. Use multiplication with the local
factor.

Exercise: ex_11_2_2.py
"""

factor = 1

def convert(kilometers):
    factor = 1000
    return kilometers * factor

print("Meters:", convert(5))
