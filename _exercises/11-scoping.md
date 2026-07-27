---
title: "Chapter 11: Scoping"
short_title: "Ch. 11 — Scoping"
layout: post
permalink: /ep/exercises/11-scoping/
order: 7
chapter: 11
exercise_count: 30
---

30 *Find the Bug* exercises from Chapter 11 of *Everyday Programming*. Every program below is short, does something recognizable, and hides **exactly one** bug — syntax, runtime, or logical. Read it, predict what it does, then run it and find out.

Worked solutions for this chapter: [Chapter 11 solutions]({{ site.baseurl }}/ep/solutions/11-scoping/). Every snippet is also available as a `.py` file — see [Exercises &amp; Solutions]({{ site.baseurl }}/ep/book/exercises/).

## Exercises 11.1.1–11.1.5

### Exercise 11.1.1 — reading a global from a function
{: #ex-11-1-1 }

This program should print the speed limit twice: once from inside `report()` and once from the top level.

```python
speed_limit_kmh = 100

def report():
    print("Inside:", speed_limit_kmh)

report()
print("Outside:", speed_limit)
# Expected:
# Inside: 100
# Outside: 100
```

[Solution 11.1.1]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-1-1) &middot; [`ex_11_1_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_1_1.py)

### Exercise 11.1.2 — a local name stays local
{: #ex-11-1-2 }

A scientist measures a temperature inside a helper function. The program should print the reading from inside the function only.

```python
def take_reading():
    temperature_c = 21.5
    print("Reading:", temperature_c)

take_reading()
print("Confirmed:", temperature_c)
# Expected:
# Reading: 21.5
```

[Solution 11.1.2]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-1-2) &middot; [`ex_11_1_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_1_2.py)

### Exercise 11.1.3 — a global constant for area
{: #ex-11-1-3 }

Using a global value of `pi`, this program should compute the area of a circle with radius 3 and print about 28.27.

```python
pi = 3.14159

def circle_area():
    area = pi * 3 * 3

circle_area()
print("Area:", area)
# expected: Area: 28.27431
```

[Solution 11.1.3]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-1-3) &middot; [`ex_11_1_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_1_3.py)

### Exercise 11.1.4 — the helper's result must come back out
{: #ex-11-1-4 }

This program should compute the perimeter of a rectangle and print it at the top level.

```python
def perimeter(length, width):
    edges = 2 * (length + width)

result = perimeter(5, 3)
print("Perimeter:", result)
# Expected:
# Perimeter: 16
```

[Solution 11.1.4]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-1-4) &middot; [`ex_11_1_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_1_4.py)

### Exercise 11.1.5 — global list, read inside the function
{: #ex-11-1-5 }

This program should print the average of a global list of test scores.

```python
scores = [80, 90, 100]

def average()
    return sum(scores) / len(scores)

print("Average:", average())
# Expected:
# Average: 90.0
```

[Solution 11.1.5]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-1-5) &middot; [`ex_11_1_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_1_5.py)

## Exercises 11.2.1–11.2.5

### Exercise 11.2.1 — local hides global, on purpose
{: #ex-11-2-1 }

The global `discount` is 0.10. Inside `checkout()` a local `discount` of 0.25 should be used for one sale, but the global should stay 0.10. The program should print the local rate then the global rate.

```python
discount = 0.10

def checkout():
    discount = 0.25
    print("Sale rate:", discount)

checkout()
print("Normal rate:", discount)
# Expected:
# Sale rate: 0.1
# Normal rate: 0.1
```

[Solution 11.2.1]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-2-1) &middot; [`ex_11_2_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_2_1.py)

### Exercise 11.2.2 — the local shadow should win inside
{: #ex-11-2-2 }

Inside `convert()`, a local `factor` should shadow the global `factor` so the function multiplies by 1000. The program should print 5000.

```python
factor = 1

def convert(kilometers):
    factor = 1000
    return kilometers / factor

print("Meters:", convert(5))
# Expected:
# Meters: 5000
```

[Solution 11.2.2]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-2-2) &middot; [`ex_11_2_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_2_2.py)

### Exercise 11.2.3 — shadowing a built-in name
{: #ex-11-2-3 }

This program should add up a list of grocery prices and print the total.

```python
prices = [2.50, 1.25, 3.00]
sum = 0

def total():
    return sum(prices)

print("Total:", total())
# Expected:
# Total: 6.75
```

[Solution 11.2.3]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-2-3) &middot; [`ex_11_2_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_2_3.py)

### Exercise 11.2.4 — which value gets printed
{: #ex-11-2-4 }

The global `tax_rate` is 0.05. Inside `quote()` a local `tax_rate` of 0.08 should be used to compute the price with tax. The program should print 108.0.

```python
tax_rate = 0.05

def quote(price):
    tax_rate = 0.08
    return price + price * 0.05

print("With tax:", quote(100))
# Expected:
# With tax: 108.0
```

[Solution 11.2.4]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-2-4) &middot; [`ex_11_2_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_2_4.py)

### Exercise 11.2.5 — parameter shadows the global
{: #ex-11-2-5 }

The global `gravity` is 9.8. The function takes its own `gravity` as a parameter so a caller can test the Moon's 1.6. The program should print the weight on the Moon.

```python
gravity = 9.8

def weight(mass, gravity):
    return mass * gravity

print("Moon weight:", weight(10, 9.8))
# Expected:
# Moon weight: 16.0
```

[Solution 11.2.5]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-2-5) &middot; [`ex_11_2_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_2_5.py)

## Exercises 11.3.1–11.3.5

### Exercise 11.3.1 — assigning makes it local
{: #ex-11-3-1 }

This program should start with a global `total` of 0 and print it unchanged after `add()` runs, because the assignment inside should create a separate local.

```python
total = 0

def add():
    total = total + 10
    print("Inside:", total)

add()
print("Outside:", total)
# Expected:
# Inside: 10
# Outside: 0
```

[Solution 11.3.1]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-3-1) &middot; [`ex_11_3_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_3_1.py)

### Exercise 11.3.2 — read before assign
{: #ex-11-3-2 }

This program should print the current step number, then set a new local step. Because `step` is assigned later in the function, the read at the top should fail unless it is read from somewhere valid.

```python
step = 1

def advance():
    print("Current:", step)
    step = step + 1

advance()
# Expected:
# Current: 1
```

[Solution 11.3.2]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-3-2) &middot; [`ex_11_3_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_3_2.py)

### Exercise 11.3.3 — counting without touching the global
{: #ex-11-3-3 }

This program should count items in a basket using a local tally and print the count, leaving the global `count` at 0.

```python
count = 0
basket = ["apple", "pear", "plum"]

def tally():
    count = 0
    for item in basket:
        count = count + item
    return count

print("Items:", tally())
# Expected:
# Items: 3
```

[Solution 11.3.3]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-3-3) &middot; [`ex_11_3_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_3_3.py)

### Exercise 11.3.4 — local sum inside a loop
{: #ex-11-3-4 }

This program should add up the distances of three trips using a local running total and print 45.

```python
distance = 0
trips = [10, 15, 20]

def trip_total():
    distance = 0
    for d in trips:
        distance = distance - d
    return distance

print("Total distance:", trip_total())
# Expected:
# Total distance: 45
```

[Solution 11.3.4]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-3-4) &middot; [`ex_11_3_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_3_4.py)

### Exercise 11.3.5 — assignment creates a fresh local
{: #ex-11-3-5 }

This program should leave the global `balance` unchanged after `spend()` runs, since the assignment inside makes a new local. The program should print 50.

```python
balance = 50

def spend():
    balance = 20

spend()
print("Balance:", balanace)
# Expected:
# Balance: 50
```

[Solution 11.3.5]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-3-5) &middot; [`ex_11_3_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_3_5.py)

## Exercises 11.4.1–11.4.5

### Exercise 11.4.1 — declaring global
{: #ex-11-4-1 }

This program should use `global` so `visitors` is increased by the function, and print 1.

```python
visitors = 0

def arrive():
    visitors = visitors + 1

arrive()
print("Visitors:", visitors)
# Expected:
# Visitors: 1
```

[Solution 11.4.1]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-4-1) &middot; [`ex_11_4_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_4_1.py)

### Exercise 11.4.2 — global then assign
{: #ex-11-4-2 }

This program should use `global` to set the module-level `score` to 100 from inside the function, and print 100.

```python
score = 0

def set_perfect():
    global score
    score == 100

set_perfect()
print("Score:", score)
# Expected:
# Score: 100
```

[Solution 11.4.2]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-4-2) &middot; [`ex_11_4_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_4_2.py)

### Exercise 11.4.3 — global keyword spelling
{: #ex-11-4-3 }

This program should use the `global` keyword so the function changes the module-level `temperature` to 25, and print 25.

```python
temperature = 0

def set_room():
    Global temperature
    temperature = 25

set_room()
print("Temperature:", temperature)
# Expected:
# Temperature: 25
```

[Solution 11.4.3]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-4-3) &middot; [`ex_11_4_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_4_3.py)

### Exercise 11.4.4 — accumulate into a global
{: #ex-11-4-4 }

This program should use `global` to add each deposit into the module-level `savings`, ending at 60.

```python
savings = 0
deposits = [10, 20, 30]

def collect():
    global savings
    for amount in deposits:
        savings = savings + amount

collect()
print("Savings:", saving)
# Expected:
# Savings: 60
```

[Solution 11.4.4]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-4-4) &middot; [`ex_11_4_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_4_4.py)

### Exercise 11.4.5 — global so the change sticks
{: #ex-11-4-5 }

This program should use `global` to flip the module-level `is_open` flag to True, and print True.

```python
is_open = False

def open_shop():
    global is_open
    is_open = false

open_shop()
print("Open:", is_open)
# Expected:
# Open: True
```

[Solution 11.4.5]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-4-5) &middot; [`ex_11_4_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_4_5.py)

## Exercises 11.5.1–11.5.5

### Exercise 11.5.1 — nonlocal counter
{: #ex-11-5-1 }

This program builds a counter with a nested function. `nonlocal` should let `increment()` change the enclosing `count`, so the two calls print 1 then 2.

```python
def make_counter():
    count = 0

    def increment():
        count = count + 1
        return count

    return increment

counter = make_counter()
print(counter())
print(counter())
# Expected:
# 1
# 2
```

[Solution 11.5.1]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-5-1) &middot; [`ex_11_5_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_5_1.py)

### Exercise 11.5.2 — running total in an enclosing scope
{: #ex-11-5-2 }

This program adds amounts into an enclosing `total` using `nonlocal`, and should print 30 after two deposits.

```python
def make_account():
    total = 0

    def deposit(amount):
        nonlocal total
        total = total - amount
        return total

    return deposit

account = make_account()
account(10)
print("Balance:", account(20))
# Expected:
# Balance: 30
```

[Solution 11.5.2]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-5-2) &middot; [`ex_11_5_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_5_2.py)

### Exercise 11.5.3 — nonlocal keyword
{: #ex-11-5-3 }

This program tracks the highest reading seen so far using `nonlocal`, and should print 9 after two readings.

```python
def make_tracker():
    highest = 0

    def record(value):
        nonlocal highest
        if value > highest:
            highest = value
        return highest

    return record

record = make_tracker()
record(4)
print("Highest:", record(9)
# Expected:
# Highest: 9
```

[Solution 11.5.3]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-5-3) &middot; [`ex_11_5_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_5_3.py)

### Exercise 11.5.4 — which scope nonlocal targets
{: #ex-11-5-4 }

This program steps a value upward by 5 each call using `nonlocal`, and should print 5 then 10.

```python
def make_stepper():
    position = 0

    def step():
        nonlocal position
        position += 5
        return position

    return step

stepper = make_stepper()
print(steper())
print(stepper())
# Expected:
# 5
# 10
```

[Solution 11.5.4]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-5-4) &middot; [`ex_11_5_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_5_4.py)

### Exercise 11.5.5 — nonlocal vs global
{: #ex-11-5-5 }

This program counts how many times a nested function runs using `nonlocal` on the enclosing `times`, and should print 2.

```python
def make_logger():
    times = 0

    def log():
        global times
        times += 1
        return times

    return log

log = make_logger()
log()
print("Times:", log())
# Expected:
# Times: 2
```

[Solution 11.5.5]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-5-5) &middot; [`ex_11_5_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_5_5.py)

## Exercises 11.6.1–11.6.5

### Exercise 11.6.1 — self attribute vs local
{: #ex-11-6-1 }

This program creates a thermometer and should print its stored temperature, 22.

```python
class Thermometer:
    def __init__(self, temperature):
        temperature = temperature

    def read(self):
        return self.temperature

device = Thermometer(22)
print("Temp:", device.read())
# Expected:
# Temp: 22
```

[Solution 11.6.1]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-6-1) &middot; [`ex_11_6_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_6_1.py)

### Exercise 11.6.2 — reading an instance attribute
{: #ex-11-6-2 }

This program stores a student's score and should print it back as 95.

```python
class Student:
    def __init__(self, score):
        self.score = score

    def get_score(self):
        return score

learner = Student(95)
print("Score:", learner.get_score())
# Expected:
# Score: 95
```

[Solution 11.6.2]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-6-2) &middot; [`ex_11_6_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_6_2.py)

### Exercise 11.6.3 — class variable shared by all
{: #ex-11-6-3 }

This program gives every `Planet` the same unit and should print "km" for two planets.

```python
class Planet:
    unit = "km"

    def __init__(self, name):
        self.name = name

earth = Planet("Earth")
mars = Planet("Mars")
print(earth.unit)
print(mars.units)
# Expected:
# km
# km
```

[Solution 11.6.3]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-6-3) &middot; [`ex_11_6_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_6_3.py)

### Exercise 11.6.4 — a local inside a method
{: #ex-11-6-4 }

This program computes a rectangle's area inside a method from stored sides and should print 12.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        result = width * self.height
        return result

box = Rectangle(3, 4)
print("Area:", box.area())
# Expected:
# Area: 12
```

[Solution 11.6.4]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-6-4) &middot; [`ex_11_6_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_6_4.py)

### Exercise 11.6.5 — updating an instance attribute
{: #ex-11-6-5 }

This program saves money into an account and should print the balance, 70, after one deposit.

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        balance = self.balance + amount

savings = Account(50)
savings.deposit(20)
print("Balance:", savings.balance)
# Expected:
# Balance: 70
```

[Solution 11.6.5]({{ site.baseurl }}/ep/solutions/11-scoping/#sol-11-6-5) &middot; [`ex_11_6_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_11_6_5.py)

