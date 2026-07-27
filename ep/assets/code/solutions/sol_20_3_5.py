"""Solution 20.3.5 — Equality used for assignment

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Runtime

speed == 60 does not create speed; the later print raises NameError. A
single = assigns the value.

Exercise: ex_20_3_5.py
"""

speed = 60
print("Speed:", speed)  # Speed: 60
