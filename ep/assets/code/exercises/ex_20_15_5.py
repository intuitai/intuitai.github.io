"""Exercise 20.15.5 — Greeting the next runner

Chapter 20: Common Pitfalls — Everyday Programming

The program should print a greeting for the runner.

This program contains exactly one bug. Solution: sol_20_15_5.py
"""

def greet_runner(name):
    return "Good luck, " + name + "!"

message = greet_runner
print(message)
