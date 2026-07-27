"""Solution 20.18.2 — Logging a temperature reading

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The file handle is never closed. Wrap the write in a with block so the
file is closed safely.

Exercise: ex_20_18_2.py
"""

with open("temps.txt", "a") as log:
    log.write("21.5\n")
