"""Solution 20.25.4 — Snapshotting weekly readings

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

readings.copy() is shallow, so the nested lists remain shared and
editing snapshot also edits readings. Use copy.deepcopy.

Exercise: ex_20_25_4.py
"""

import copy

readings = [[1.0, 2.0], [3.0, 4.0]]
snapshot = copy.deepcopy(readings)
snapshot[0][0] = 99.0
print("Readings:", readings)  # Readings: [[1.0, 2.0], [3.0, 4.0]]
