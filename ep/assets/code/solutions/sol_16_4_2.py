"""Solution 16.4.2 — Releasing the scale

Chapter 16: Handling Failures — Everyday Programming

Bug type: Logical

“Scale released” must always print, but it is in the else block, which
runs only when no exception occurs; on bad input it is skipped. Use
finally so it runs whether or not an error happened.

Exercise: ex_16_4_2.py
"""

try:
    weight = float(input("Weight in kilograms? "))
    print("Recorded weight:", weight)
except ValueError:
    print("That was not a number.")
finally:
    print("Scale released.")
