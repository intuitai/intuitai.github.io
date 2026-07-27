"""Solution 11.3.5 — assignment creates a fresh local

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

The final print reads balanace, a misspelling, so Python raises
NameError. Use the correct global name balance.

Exercise: ex_11_3_5.py
"""

balance = 50

def spend():
    balance = 20

spend()
print("Balance:", balance)
