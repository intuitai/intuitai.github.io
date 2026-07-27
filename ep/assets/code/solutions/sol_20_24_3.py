"""Solution 20.24.3 — Kinetic energy of a moving cart

Chapter 20: Common Pitfalls — Everyday Programming

Bug type: Logical

The speed must be squared (speed 2), but the code multiplies by 2
instead. Testing the squaring step alone would reveal this.

Exercise: ex_20_24_3.py
"""

def kinetic_energy(mass, speed):
    return 0.5 * mass * speed ** 2

print("Kinetic energy:", kinetic_energy(2, 3))  # Kinetic energy: 9.0
