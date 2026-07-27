"""Exercise 6.3.2 — Same behavior, different types

Chapter 6: Objects — Everyday Programming

Any object that can speak() can be greeted, regardless of its class.

This program contains exactly one bug. Solution: sol_6_3_2.py
"""

class Cat:
    def speak(self):
        return "Meow"

class Cow:
    def speak(self):
        return "Moo"

def greet(animal):
    print("The animal says:", animal.speka())

greet(Cat())
greet(Cow())   # The animal says: Moo
