"""Solution 11.5.4 — which scope nonlocal targets

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

The first call uses steper(), a misspelling of stepper, so Python raises
NameError. Use the correct name.

Exercise: ex_11_5_4.py
"""

def make_stepper():
    position = 0

    def step():
        nonlocal position
        position += 5
        return position

    return step

stepper = make_stepper()
print(stepper())
print(stepper())
