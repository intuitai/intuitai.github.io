"""Exercise 6.2.3 — Updating a class counter

Chapter 6: Objects — Everyday Programming

A class attribute should count how many books have been created.

This program contains exactly one bug. Solution: sol_6_2_3.py
"""

class Book:
    count = 0

    def __init__(self, title):
        self.title = title
        self.count = self.count + 1

Book("Algebra")
Book("Biology")
Book("Chemistry")
print(Book.count)   # 3
