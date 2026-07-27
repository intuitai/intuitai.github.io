"""Exercise 20.25.5 — Cloning a recipe with sub-steps

Chapter 20: Common Pitfalls — Everyday Programming

This program should clone a recipe (with nested steps) so editing the
clone is safe.

This program contains exactly one bug. Solution: sol_20_25_5.py
"""

import copy

recipe = [["mix", "stir"], ["bake", "cool"]]
clone = recipe[:]
clone[1].append("serve")
print("Recipe:", recipe)  # Recipe: [['mix', 'stir'], ['bake', 'cool']]
