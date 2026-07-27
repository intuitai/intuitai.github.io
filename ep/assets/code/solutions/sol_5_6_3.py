"""Solution 5.6.3 — Last score

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

The list has indexes 0, 1, 2, so scores[3] is out of range and raises an
IndexError. The last item is at index 2 (or use -1).

Exercise: ex_5_6_3.py
"""

scores = [70, 95, 88]
print(scores[-1])   # 88
