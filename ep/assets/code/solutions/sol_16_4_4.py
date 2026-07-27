"""Solution 16.4.4 — Final tally

Chapter 16: Handling Failures — Everyday Programming

Bug type: Logical

The tally line sits inside the try right after the division, so a
ZeroDivisionError skips it. A line that must always run belongs in a
finally block, which executes whether or not an exception occurs.

Exercise: ex_16_4_4.py
"""

points = 90
rounds = 0
try:
    average = points / rounds
    print("Average:", average)
except ZeroDivisionError:
    print("No rounds played.")
finally:
    print("Final tally complete.")
