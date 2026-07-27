"""Solution 16.2.3 — Average speed

Chapter 16: Handling Failures — Everyday Programming

Bug type: Logical

The broad except Exception is listed first, and because
ZeroDivisionError is a subclass of Exception, the first handler swallows
a zero-time error and prints the misleading “Distance was not a number”
message; the specific ZeroDivisionError handler is unreachable. Put the
specific handler before the general one.

Exercise: ex_16_2_3.py
"""

distance = float(input("Distance in meters? "))
time = float(input("Time in seconds? "))
try:
    speed = distance / time
    print("Average speed:", speed)
except ZeroDivisionError:
    print("Time cannot be zero.")
except Exception:
    print("Distance was not a number.")
