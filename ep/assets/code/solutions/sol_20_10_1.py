"""Solution 20.10.1 — Setting a fourth temperature

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

readings has indexes 0–2, so assigning to readings[3] raises IndexError;
assignment cannot grow a list. Use append to add a fourth value.

Exercise: ex_20_10_1.py
"""

readings = [20, 22, 21]
readings.append(23)
print(readings)
