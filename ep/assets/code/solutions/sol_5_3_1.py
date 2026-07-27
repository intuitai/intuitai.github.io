"""Solution 5.3.1 — Is it freezing?

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

"Below freezing" means less than 0, but the test used >, which is False
for -5. Use < so the comparison returns True.

Exercise: ex_5_3_1.py
"""

temp = -5
is_freezing = temp < 0
print(is_freezing)   # True
