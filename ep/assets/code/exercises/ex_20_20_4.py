"""Exercise 20.20.4 — Looking up a city name

Chapter 20: Common Pitfalls — Everyday Programming

The program should find "Paris" in the list even if typed in lowercase.

This program contains exactly one bug. Solution: sol_20_20_4.py
"""

cities = ["Paris", "London", "Tokyo"]
search = "paris"
if search in cities:
    print("City found")
else:
    print("City not found")
