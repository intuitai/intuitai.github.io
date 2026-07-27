"""Exercise 11.3.5 — assignment creates a fresh local

Chapter 11: Scoping — Everyday Programming

This program should leave the global balance unchanged after spend()
runs, since the assignment inside makes a new local. The program should
print 50.

This program contains exactly one bug. Solution: sol_11_3_5.py
"""

balance = 50

def spend():
    balance = 20

spend()
print("Balance:", balanace)
# Expected:
# Balance: 50
