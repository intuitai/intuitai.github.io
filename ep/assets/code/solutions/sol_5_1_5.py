"""Solution 5.1.5 — Apples per box

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

% gives the remainder (2 leftover apples), not the number of full boxes.
Use integer division // to get 3.

Exercise: ex_5_1_5.py
"""

apples = 17
per_box = 5

full_boxes = apples // per_box
print(full_boxes)   # 3
