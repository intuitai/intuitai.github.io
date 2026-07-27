"""Solution 7.2.1 — Saving up for a bike

Chapter 7: Operators — Everyday Programming

Bug type: Logical

The second line uses plain assignment = and overwrites the starting $60
with $45, so the final total is wrong. It should be augmented assignment
+= to add the deposit.

Exercise: ex_7_2_1.py
"""

savings = 60
savings += 45
savings += 45
print(savings)   # 150
