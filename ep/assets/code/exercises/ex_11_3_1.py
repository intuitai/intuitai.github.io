"""Exercise 11.3.1 — assigning makes it local

Chapter 11: Scoping — Everyday Programming

This program should start with a global total of 0 and print it
unchanged after add() runs, because the assignment inside should create
a separate local.

This program contains exactly one bug. Solution: sol_11_3_1.py
"""

total = 0

def add():
    total = total + 10
    print("Inside:", total)

add()
print("Outside:", total)
# Expected:
# Inside: 10
# Outside: 0
