"""Solution 20.26.3 — Logging a single temperature

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The default log=[] is created once and reused across calls, so readings
accumulate. Default to None and build a fresh list.

Exercise: ex_20_26_3.py
"""

def log_reading(reading, log=None):
    if log is None:
        log = []
    log.append(reading)
    return log

print(log_reading(21.5))  # [21.5]
print(log_reading(19.0))  # [19.0]
