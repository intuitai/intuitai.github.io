"""Solution 20.3.3 — Equality used where assignment is meant

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

balance == 100 compares instead of assigning, so balance is never
created and the print raises NameError. Use a single = to assign.

Exercise: ex_20_3_3.py
"""

balance = 100
print(balance)  # 100
