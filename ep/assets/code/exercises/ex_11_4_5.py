"""Exercise 11.4.5 — global so the change sticks

Chapter 11: Scoping — Everyday Programming

This program should use global to flip the module-level is_open flag to
True, and print True.

This program contains exactly one bug. Solution: sol_11_4_5.py
"""

is_open = False

def open_shop():
    global is_open
    is_open = false

open_shop()
print("Open:", is_open)
# Expected:
# Open: True
