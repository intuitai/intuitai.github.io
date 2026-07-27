"""Exercise 5.9.3 — Missing key

Chapter 5: Data Structures — Everyday Programming

The program should safely look up a missing subject and print "not
found" instead of crashing.

This program contains exactly one bug. Solution: sol_5_9_3.py
"""

student = {"name": "Maya", "grade": 10}
subject = student["favorite_subject"]
print(subject)   # not found
