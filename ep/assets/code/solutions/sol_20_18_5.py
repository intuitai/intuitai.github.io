"""Solution 20.18.5 — Storing a measured weight

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

weight_file is never closed, risking unflushed data. Use a with block to
close it safely.

Exercise: ex_20_18_5.py
"""

weight_kg = 72.4
with open("weight.txt", "w") as weight_file:
    weight_file.write(f"{weight_kg}\n")
