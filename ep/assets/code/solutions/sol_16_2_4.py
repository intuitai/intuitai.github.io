"""Solution 16.2.4 — Looking up a grade

Chapter 16: Handling Failures — Everyday Programming

Bug type: Runtime

Looking up a missing dictionary key raises KeyError, but the code
catches ValueError, so the lookup failure is not handled and the program
crashes. Catch KeyError.

Exercise: ex_16_2_4.py
"""

grades = {"Ann": 91, "Bo": 84}
name = "Cleo"
try:
    print(name, "scored", grades[name])
except KeyError:
    print("No grade recorded for", name)
