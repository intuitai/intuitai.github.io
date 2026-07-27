"""Exercise 20.24.3 — Kinetic energy of a moving cart

Chapter 20: Common Pitfalls — Everyday Programming

This program should compute kinetic energy (one-half m v squared) for
m=2, v=3 and print 9.0.

This program contains exactly one bug. Solution: sol_20_24_3.py
"""

def kinetic_energy(mass, speed):
    return 0.5 * mass * speed * 2

print("Kinetic energy:", kinetic_energy(2, 3))  # Kinetic energy: 9.0
