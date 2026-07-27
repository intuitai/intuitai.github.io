"""Solution 20.12.2 — Collecting daily steps

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

steps is a tuple, so append raises AttributeError. Use brackets to
create a list.

Exercise: ex_20_12_2.py
"""

steps = [8000, 9500, 7000]
steps.append(10000)
print(steps)
