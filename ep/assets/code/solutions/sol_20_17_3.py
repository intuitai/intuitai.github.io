"""Solution 20.17.3 — Counting visitors

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Because visitors is assigned inside enter, Python marks it local and
raises UnboundLocalError. Declare it global.

Exercise: ex_20_17_3.py
"""

visitors = 0

def enter():
    global visitors
    visitors = visitors + 1

enter()
print("Visitors:", visitors)
