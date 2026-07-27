"""Solution 7.2.5 — Running total of steps

Chapter 7: Operators — Everyday Programming

Bug type: Logical

The line computes total_steps + today_steps but throws the result away
because it never assigns it back. Use += so the running total is
updated.

Exercise: ex_7_2_5.py
"""

total_steps = 6000
today_steps = 4000
total_steps += today_steps
print(total_steps)   # 10000
