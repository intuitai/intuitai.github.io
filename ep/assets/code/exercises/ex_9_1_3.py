"""Exercise 9.1.3 — Independent checks that should be alternatives

Chapter 9: Control Flow — Everyday Programming

A water sample's pH should be labelled once: acidic, neutral, or basic.
With pH 6.0 it should print only Acidic.

This program contains exactly one bug. Solution: sol_9_1_3.py
"""

ph = 6.0

if ph < 7:
    print("Acidic")
if ph == 7:
    print("Neutral")
else:
    print("Basic")
