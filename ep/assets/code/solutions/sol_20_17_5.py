"""Solution 20.17.5 — Building a points streak

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

streak is assigned inside the function, so Python treats it as local and
raises UnboundLocalError. Declare it global.

Exercise: ex_20_17_5.py
"""

streak = 1

def double_streak():
    global streak
    streak = streak * 2

double_streak()
print("Streak:", streak)
