"""Solution 17.1.2 — Celsius to Fahrenheit check

Chapter 17: Testing — Everyday Programming

Bug type: Logical

The function is correct, but the expected value in the test is wrong:
100 °C is 212 °F, not 211. The fix corrects the expected value.

Exercise: ex_17_1_2.py
"""

def c_to_f(celsius):
    return celsius * 9 / 5 + 32

assert c_to_f(100) == 212
print("passed")
