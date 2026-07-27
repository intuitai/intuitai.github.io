"""Solution 5.8.2 — Adding a member

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

Sets have no append method, so this raises an AttributeError. Use add to
put an item in a set.

Exercise: ex_5_8_2.py
"""

cities = {"New York", "London", "Tokyo"}
cities.add("Sydney")
print(len(cities))   # 4
