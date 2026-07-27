"""Solution 20.6.4 — Combining a count with text

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

books + " books..." adds an int to a string, raising TypeError. Convert
books to a string first.

Exercise: ex_20_6_4.py
"""

books = 12
print(str(books) + " books on the shelf")
