"""Solution 5.6.2 — Adding an item

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

Lists have no add method, so this raises an AttributeError. Use append
to add to a list.

Exercise: ex_5_6_2.py
"""

fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(len(fruits))   # 4
