"""Solution 20.10.5 — Appending a measurement

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Assigning to ph_values[3] on a three-item list raises IndexError. Use
append to add a new reading.

Exercise: ex_20_10_5.py
"""

ph_values = [7.0, 6.8, 7.2]
ph_values.append(6.9)
print(ph_values)
