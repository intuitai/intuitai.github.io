"""Solution 5.9.3 — Missing key

Chapter 5: Data Structures — Everyday Programming

Bug type: Runtime

Indexing a missing key with [] raises a KeyError. Use .get with a
default so it returns "not found" instead.

Exercise: ex_5_9_3.py
"""

student = {"name": "Maya", "grade": 10}
subject = student.get("favorite_subject", "not found")
print(subject)   # not found
