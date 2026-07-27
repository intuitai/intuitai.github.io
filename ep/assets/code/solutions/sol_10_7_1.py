"""Solution 10.7.1 — No return means None

Chapter 10: Functions — Everyday Programming

Bug type: Logical

The function explicitly returns "done", so result is not None. Remove
the return so the function returns None implicitly.

Exercise: ex_10_7_1.py
"""

def announce():
    print("The meeting starts now.")

result = announce()
print(result)  # None
