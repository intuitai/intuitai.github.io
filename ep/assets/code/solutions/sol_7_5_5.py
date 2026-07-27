"""Solution 7.5.5 — Day in the schedule

Chapter 7: Operators — Everyday Programming

Bug type: Logical

not in returns False when the day is present, the reverse of what we
want. Use the in operator to confirm membership.

Exercise: ex_7_5_5.py
"""

schedule = ["Monday", "Wednesday", "Friday"]
has_wednesday = "Wednesday" in schedule
print(has_wednesday)   # True
