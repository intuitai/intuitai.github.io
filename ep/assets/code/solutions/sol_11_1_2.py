"""Solution 11.1.2 — a local name stays local

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

temperature_c is local to take_reading(), so it does not exist at the
top level; the final print raises NameError. Remove that line (a local
name is not visible outside its function).

Exercise: ex_11_1_2.py
"""

def take_reading():
    temperature_c = 21.5
    print("Reading:", temperature_c)

take_reading()
