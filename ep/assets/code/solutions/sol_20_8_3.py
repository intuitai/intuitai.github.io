"""Solution 20.8.3 — Counting full boxes

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

40 / 6 is 6.66..., but you can only fill whole boxes. // gives the
correct 6.

Exercise: ex_20_8_3.py
"""

eggs = 40
per_box = 6
full_boxes = eggs // per_box
print(full_boxes)  # 6
