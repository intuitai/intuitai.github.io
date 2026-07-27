"""Solution 20.5.2 — Misspelled variable in a calculation

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

sped was never defined; only speed exists, so the line raises NameError.
Fix the spelling.

Exercise: ex_20_5_2.py
"""

speed = 60
hours = 2
distance = speed * hours
print(distance)  # 120
