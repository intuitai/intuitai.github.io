"""Solution 16.2.1 — Splitting a bill

Chapter 16: Handling Failures — Everyday Programming

Bug type: Runtime

Dividing by zero raises ZeroDivisionError, but the code catches
ValueError, so the real error escapes and the program crashes. Catch
ZeroDivisionError.

Exercise: ex_16_2_1.py
"""

bill = 60.0
friends = 0
try:
    share = bill / friends
    print("Each person pays", share)
except ZeroDivisionError:
    print("There must be at least one person.")
