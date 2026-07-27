"""Solution 7.1.4 — Kinetic energy

Chapter 7: Operators — Everyday Programming

Bug type: Logical

The formula multiplies speed by 2 instead of squaring it, giving 6.0
rather than 9.0. Use the power operator to square the speed.

Exercise: ex_7_1_4.py
"""

mass = 2
speed = 3
energy = 0.5 * mass * speed ** 2
print(energy)   # 9.0
