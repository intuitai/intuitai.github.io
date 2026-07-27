"""Exercise 11.2.2 — the local shadow should win inside

Chapter 11: Scoping — Everyday Programming

Inside convert(), a local factor should shadow the global factor so the
function multiplies by 1000. The program should print 5000.

This program contains exactly one bug. Solution: sol_11_2_2.py
"""

factor = 1

def convert(kilometers):
    factor = 1000
    return kilometers / factor

print("Meters:", convert(5))
# Expected:
# Meters: 5000
