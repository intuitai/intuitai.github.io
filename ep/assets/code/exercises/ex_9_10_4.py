"""Exercise 9.10.4 — Default case

Chapter 9: Control Flow — Everyday Programming

This program should print Unknown command for anything it does not
recognize. For "fly" it should print Unknown command.

This program contains exactly one bug. Solution: sol_9_10_4.py
"""

command = "fly"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "_":
        print("Unknown command")
# Expected: Unknown command
