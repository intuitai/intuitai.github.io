"""Solution 20.10.4 — Adding a fourth runner's time

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

len(lap_times) is 3, which is one past the last valid index, so the
assignment raises IndexError. Use append.

Exercise: ex_20_10_4.py
"""

lap_times = [45, 47, 44]
lap_times.append(46)
print(lap_times)
