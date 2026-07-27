"""Solution 18.4.1 — Total grocery cost

Chapter 18: Bugs — Everyday Programming

Bug type: Logical

Printing the subtotal reveals it is too low: the milk price is
subtracted instead of added. Changing the - to + totals all three items.

Exercise: ex_18_4_1.py
"""

def total_cost(apples, bread, milk):
    subtotal = apples + bread + milk
    return subtotal

print(total_cost(3.50, 2.25, 1.75))   # 7.5
