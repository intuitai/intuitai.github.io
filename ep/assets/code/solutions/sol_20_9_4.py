"""Solution 20.9.4 — Volume of a cube

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

3 ^ 3 is XOR (0), not 3 cubed. Use to raise to a power.

Exercise: ex_20_9_4.py
"""

edge = 3
volume = edge ** 3
print(volume)  # 27
