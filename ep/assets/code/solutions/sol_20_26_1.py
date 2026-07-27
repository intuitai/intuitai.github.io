"""Solution 20.26.1 — Collecting quiz answers

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The default sheet=[] is created once and reused, so answers accumulate
across calls. Default to None and make a fresh list inside.

Exercise: ex_20_26_1.py
"""

def record_answer(answer, sheet=None):
    if sheet is None:
        sheet = []
    sheet.append(answer)
    return sheet

print(record_answer("A"))  # ['A']
print(record_answer("B"))  # ['B']
