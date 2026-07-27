"""Exercise 20.18.1 — Saving a shopping list

Chapter 20: Common Pitfalls — Everyday Programming

This program should write the shopping list to a file and leave no file
handle open.

This program contains exactly one bug. Solution: sol_20_18_1.py
"""

groceries = "milk\neggs\nbread\n"
list_file = open("groceries.txt", "w")
list_file.write(groceries)
print("Shopping list saved")
