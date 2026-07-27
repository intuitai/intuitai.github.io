"""Exercise 10.4.1 — A default value

Chapter 10: Functions — Everyday Programming

This program should print a greeting with the default name when called
with no argument.

This program contains exactly one bug. Solution: sol_10_4_1.py
"""

def greet(name="friend"):
    print("Hello,", name)

greet
