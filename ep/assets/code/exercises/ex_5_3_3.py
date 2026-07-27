"""Exercise 5.3.3 — Both lights on

Chapter 5: Data Structures — Everyday Programming

A room is "ready" only if both lights are on. The program should print
False here, since one light is off.

This program contains exactly one bug. Solution: sol_5_3_3.py
"""

light1_on = True
light2_on = False

ready = light1_on or light2_on
print(ready)   # False
