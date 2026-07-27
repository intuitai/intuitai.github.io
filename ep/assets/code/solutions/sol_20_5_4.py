"""Solution 20.5.4 — Misspelled variable when updating

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

bil is a misspelling of bill, so the calculation raises NameError. Use
the correct name.

Exercise: ex_20_5_4.py
"""

bill = 40
tip = 6
total = bill + tip
print(total)  # 46
