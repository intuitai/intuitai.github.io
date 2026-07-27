"""Exercise 20.18.2 — Logging a temperature reading

Chapter 20: Common Pitfalls — Everyday Programming

The program should append one temperature reading to a log file safely.

This program contains exactly one bug. Solution: sol_20_18_2.py
"""

log = open("temps.txt", "a")
log.write("21.5\n")
