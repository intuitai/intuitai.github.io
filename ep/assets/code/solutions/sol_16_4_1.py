"""Solution 16.4.1 — Closing a report

Chapter 16: Handling Failures — Everyday Programming

Bug type: Logical

The closing line sits inside the except block, so it prints only when
the division fails; on the normal path it never runs. Move the always-
run line into a finally block.

Exercise: ex_16_4_1.py
"""

try:
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Done with the calculation.")
