"""Exercise 20.26.1 — Collecting quiz answers

Chapter 20: Common Pitfalls — Everyday Programming

Each call should start with an empty answer sheet and add one answer.

This program contains exactly one bug. Solution: sol_20_26_1.py
"""

def record_answer(answer, sheet=[]):
    sheet.append(answer)
    return sheet

print(record_answer("A"))  # ['A']
print(record_answer("B"))  # ['B']
