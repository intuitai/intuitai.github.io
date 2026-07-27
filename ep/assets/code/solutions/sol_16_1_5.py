"""Solution 16.1.5 — Validating a test score

Chapter 16: Handling Failures — Everyday Programming

Bug type: Logical

The except block silently keeps the invalid text by assigning score =
raw, so the program reports nonsense as a score instead of rejecting it.
Validation should re-prompt or refuse bad input rather than swallow it.

Exercise: ex_16_1_5.py
"""

while True:
    raw = input("Enter your test score: ")
    try:
        score = int(raw)
        break
    except ValueError:
        print("Please type a whole number.")
print("Your score is", score)
