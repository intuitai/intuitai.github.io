"""Exercise 5.9.4 — Safe default with get

Chapter 5: Data Structures — Everyday Programming

Using .get, the program should print "science" when the key exists.

This program contains exactly one bug. Solution: sol_5_9_4.py
"""

student = {"favorite_subject": "science"}
subject = student.get("favorite_subject", "unknown")
print(Subject)   # science
