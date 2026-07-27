"""Solution 20.17.1 — Tallying rainfall

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

Assigning to total_rain inside the function makes it local, so reading
it on the right raises UnboundLocalError. Declare it global.

Exercise: ex_20_17_1.py
"""

total_rain = 0.0

def add_rain(today):
    global total_rain
    total_rain = total_rain + today

add_rain(1.2)
print("Total rainfall:", total_rain)
