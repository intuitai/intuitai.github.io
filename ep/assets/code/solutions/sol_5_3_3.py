"""Solution 5.3.3 — Both lights on

Chapter 5: Data Structures — Everyday Programming

Bug type: Logical

"Both" requires and; or is True when either light is on. Use and so the
result is False here.

Exercise: ex_5_3_3.py
"""

light1_on = True
light2_on = False

ready = light1_on and light2_on
print(ready)   # False
