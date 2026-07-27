"""Solution 20.20.4 — Looking up a city name

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The list stores "Paris", so a lowercase "paris" is not found. Compare in
a consistent case, for example by lowercasing each city.

Exercise: ex_20_20_4.py
"""

cities = ["Paris", "London", "Tokyo"]
search = "paris"
if search in [city.lower() for city in cities]:
    print("City found")
else:
    print("City not found")
