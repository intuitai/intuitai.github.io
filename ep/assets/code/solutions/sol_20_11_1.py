"""Solution 20.11.1 — Reading the last color

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Indexes run 0–2, so colors[3] is out of range and raises IndexError. The
last item is at index 2.

Exercise: ex_20_11_1.py
"""

colors = ["red", "green", "blue"]
print(colors[2])
