"""Solution 10.5.3 — Spelling the keyword

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The keyword temp does not match the parameter temperature, raising a
TypeError. Use the exact parameter name.

Exercise: ex_10_5_3.py
"""

def report(city, temperature):
    print(city, "is at", temperature, "degrees")

report(city="Denver", temperature=30)
