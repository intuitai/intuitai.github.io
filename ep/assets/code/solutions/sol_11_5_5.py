"""Solution 11.5.5 — nonlocal vs global

Chapter 11: Scoping — Everyday Programming

Bug type: Runtime

times lives in the enclosing function, not the module, so global times
cannot find it and raises NameError at call time. Use nonlocal to target
the enclosing scope.

Exercise: ex_11_5_5.py
"""

def make_logger():
    times = 0

    def log():
        nonlocal times
        times += 1
        return times

    return log

log = make_logger()
log()
print("Times:", log())
