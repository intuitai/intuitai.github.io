"""Solution 11.4.4 — accumulate into a global

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

The final print reads saving, but the global is savings, so Python
raises NameError. Use the correct name.

Exercise: ex_11_4_4.py
"""

savings = 0
deposits = [10, 20, 30]

def collect():
    global savings
    for amount in deposits:
        savings = savings + amount

collect()
print("Savings:", savings)
