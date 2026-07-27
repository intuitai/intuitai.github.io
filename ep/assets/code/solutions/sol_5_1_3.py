"""Solution 5.1.3 — Seconds in an hour

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

The two counts must be multiplied, not added; 60 + 60 gives 120, not
3600. Use *.

Exercise: ex_5_1_3.py
"""

seconds_per_minute = 60
minutes_per_hour = 60

seconds_per_hour = seconds_per_minute * minutes_per_hour
print(seconds_per_hour)   # 3600
