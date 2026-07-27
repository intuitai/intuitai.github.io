"""Exercise 20.18.5 — Storing a measured weight

Chapter 20: Common Pitfalls — Everyday Programming

This program should save a measured weight in kilograms to a file
safely.

This program contains exactly one bug. Solution: sol_20_18_5.py
"""

weight_kg = 72.4
weight_file = open("weight.txt", "w")
weight_file.write(f"{weight_kg}\n")
