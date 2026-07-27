"""Solution 20.11.2 — Printing each day's high

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

range(5) reaches index 4, but the list has only indexes 0–3, so the loop
raises IndexError. Loop to len(highs) (or iterate the list directly).

Exercise: ex_20_11_2.py
"""

highs = [28, 30, 29, 31]
for i in range(len(highs)):
    print(highs[i])
