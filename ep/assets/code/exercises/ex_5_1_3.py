"""Exercise 5.1.3 — Seconds in an hour

Chapter 5: Data Structures — Everyday Programming

There are 60 seconds in a minute and 60 minutes in an hour. The program
should print 3600.

This program contains exactly one bug. Solution: sol_5_1_3.py
"""

seconds_per_minute = 60
minutes_per_hour = 60

seconds_per_hour = seconds_per_minute + minutes_per_hour
print(seconds_per_hour)   # 3600
