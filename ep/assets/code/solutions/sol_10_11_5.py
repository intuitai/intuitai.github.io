"""Solution 10.11.5 — Checking for None

Chapter 10: Functions — Everyday Programming

Bug type: Runtime

The default is None, but the guard checks == [], which is never true for
None, so days.append raises an AttributeError on the first call. Check
is None.

Exercise: ex_10_11_5.py
"""

def append_day(day, days=None):
    if days is None:
        days = []
    days.append(day)
    return days

print(append_day("Mon"))  # ['Mon']
print(append_day("Tue"))  # ['Tue']
