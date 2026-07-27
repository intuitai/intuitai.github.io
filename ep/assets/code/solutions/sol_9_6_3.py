"""Solution 9.6.3 — Doubling savings

Chapter 9: Control Flow — Everyday Programming

Bug type: Logical

balance + 2 adds a fixed 2 each pass instead of *doubling*, so the
balance grows 1, 3, 5, 7, ... and the values are wrong. Multiplying by 2
doubles it as intended.

Exercise: ex_9_6_3.py
"""

balance = 1

while balance < 8:
    print(balance)
    balance = balance * 2
