"""Solution 20.14.3 — Confirming a recipe title

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The title built by concatenation is a separate string object, so is
returns False even when the text is identical. Use == to compare the
values.

Exercise: ex_20_14_3.py
"""

saved_title = "Banana Bread"
first = "Banana"
second = "Bread"
built_title = first + " " + second
if built_title == saved_title:
    print("Recipe title matches")
else:
    print("Recipe title differs")
