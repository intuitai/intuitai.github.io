"""Exercise 20.26.3 — Logging a single temperature

Chapter 20: Common Pitfalls — Everyday Programming

Each call should return a new log holding only the reading passed in.

This program contains exactly one bug. Solution: sol_20_26_3.py
"""

def log_reading(reading, log=[]):
    log.append(reading)
    return log

print(log_reading(21.5))  # expected [21.5]
print(log_reading(19.0))  # expected [19.0]
