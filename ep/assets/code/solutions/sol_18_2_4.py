"""Solution 18.2.4 — Last student's score

Chapter 18: Bugs — Everyday Programming

Bug type: Runtime

len(scores) is 4, but valid indices run 0 to 3, so scores[4] raises
IndexError. The last element is at index len(scores) - 1 (or simply -1).

Exercise: ex_18_2_4.py
"""

scores = [88, 91, 79, 95]
last_index = len(scores) - 1
print(scores[last_index])   # 95
