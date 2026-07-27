"""Exercise 20.18.4 — Writing a daily journal entry

Chapter 20: Common Pitfalls — Everyday Programming

The program should write one journal line to a file safely.

This program contains exactly one bug. Solution: sol_20_18_4.py
"""

entry = "Today I walked 10000 steps.\n"
journal = open("journal.txt", "w")
journal.write(entry)
print("Entry written")
