"""Solution 20.18.1 — Saving a shopping list

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The file is opened but never closed, so the handle leaks and buffered
data may not flush. Use a with block, which closes automatically.

Exercise: ex_20_18_1.py
"""

groceries = "milk\neggs\nbread\n"
with open("groceries.txt", "w") as list_file:
    list_file.write(groceries)
print("Shopping list saved")
