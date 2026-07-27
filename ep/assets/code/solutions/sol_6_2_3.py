"""Solution 6.2.3 — Updating a class counter

Chapter 6: Objects — Everyday Programming

Bug type: Logical

Writing self.count = self.count + 1 reads the class value but creates a
new *instance* attribute, leaving Book.count at 0. Incrementing
Book.count updates the shared class counter, so it reaches 3.

Exercise: ex_6_2_3.py
"""

class Book:
    count = 0

    def __init__(self, title):
        self.title = title
        Book.count = Book.count + 1

Book("Algebra")
Book("Biology")
Book("Chemistry")
print(Book.count)   # 3
