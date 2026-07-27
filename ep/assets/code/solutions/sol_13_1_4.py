"""Solution 13.1.4 — Average test score

Chapter 13: Modules — Everyday Programming

Bug type: Runtime

The module was imported as statistics, but the call uses statistic
(missing the final s), raising NameError. Use the same name in the call
that you used in the import.

Exercise: ex_13_1_4.py
"""

import statistics

scores = [80, 90, 100, 70]
average = statistics.mean(scores)
print(statistics.mean(scores))   # 85
