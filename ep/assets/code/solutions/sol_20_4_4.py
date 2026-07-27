"""Solution 20.4.4 — Reading a counter that is set later

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

laps is used before it is created, so the print raises NameError. Assign
laps before printing it.

Exercise: ex_20_4_4.py
"""

laps = 4
print("Laps:", laps)
