"""Exercise 5.1.5 — Apples per box

Chapter 5: Data Structures — Everyday Programming

You have 17 apples and want 5 per box. The program should print how many
full boxes (3) you can fill.

This program contains exactly one bug. Solution: sol_5_1_5.py
"""

apples = 17
per_box = 5

full_boxes = apples % per_box
print(full_boxes)   # 3
