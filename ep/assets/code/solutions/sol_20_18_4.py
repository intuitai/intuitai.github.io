"""Solution 20.18.4 — Writing a daily journal entry

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The file is left open. A with block guarantees the file is closed even
if an error occurs.

Exercise: ex_20_18_4.py
"""

entry = "Today I walked 10000 steps.\n"
with open("journal.txt", "w") as journal:
    journal.write(entry)
print("Entry written")
