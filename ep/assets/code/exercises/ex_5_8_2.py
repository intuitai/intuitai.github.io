"""Exercise 5.8.2 — Adding a member

Chapter 5: Data Structures — Everyday Programming

The program should add "Sydney" to the set of cities and print 4 members
in total.

This program contains exactly one bug. Solution: sol_5_8_2.py
"""

cities = {"New York", "London", "Tokyo"}
cities.append("Sydney")
print(len(cities))   # 4
