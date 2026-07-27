"""Solution 20.25.5 — Cloning a recipe with sub-steps

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

Slicing with [:] copies only the outer list; the nested step lists are
shared, so appending through clone changes recipe. Use copy.deepcopy.

Exercise: ex_20_25_5.py
"""

import copy

recipe = [["mix", "stir"], ["bake", "cool"]]
clone = copy.deepcopy(recipe)
clone[1].append("serve")
print("Recipe:", recipe)  # Recipe: [['mix', 'stir'], ['bake', 'cool']]
