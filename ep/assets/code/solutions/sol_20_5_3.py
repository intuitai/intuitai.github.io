"""Solution 20.5.3 — Inconsistent capitalization

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Python is case-sensitive: Temperature and temperature are different
names, so the print raises NameError. Match the case used at assignment.

Exercise: ex_20_5_3.py
"""

Temperature = 31
print(Temperature)
