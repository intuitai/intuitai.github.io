"""Exercise 8.1.4 — Saving a temperature reading

Chapter 8: Input and Output — Everyday Programming

This program writes one weather reading to a file and then prints it
back.

This program contains exactly one bug. Solution: sol_8_1_4.py
"""

with open("reading.txt", "w", encoding="utf-8") as f:
    f.write("Tokyo,36.5\n")

with open("reading.txt", "w", encoding="utf-8") as f:
    contents = f.read()

print(contents)
