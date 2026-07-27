"""Exercise 6.4.5 — A list method

Chapter 6: Objects — Everyday Programming

This program removes a finished task from the to-do list.

This program contains exactly one bug. Solution: sol_6_4_5.py
"""

tasks = ["email", "report", "lunch"]
tasks.remove(1)
print(tasks)   # ['email', 'lunch']
