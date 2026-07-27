---
title: "Chapter 6: Objects"
short_title: "Ch. 6 — Objects"
layout: post
permalink: /ep/exercises/06-objects/
order: 2
chapter: 6
exercise_count: 25
---

25 *Find the Bug* exercises from Chapter 6 of *Everyday Programming*. Every program below is short, does something recognizable, and hides **exactly one** bug — syntax, runtime, or logical. Read it, predict what it does, then run it and find out.

Worked solutions for this chapter: [Chapter 6 solutions]({{ site.baseurl }}/ep/solutions/06-objects/). Every snippet is also available as a `.py` file — see [Exercises &amp; Solutions]({{ site.baseurl }}/ep/book/exercises/).

## Exercises 6.1.1–6.1.5

### Exercise 6.1.1 — Defining a class
{: #ex-6-1-1 }

This class should store a rectangle's width and height and report its area.

```python
class Rectangle:
    def __init__(self, width, height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

room = Rectangle(4, 3)
print(room.area())   # 12
```

[Solution 6.1.1]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-1-1) &middot; [`ex_6_1_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_1_1.py)

### Exercise 6.1.2 — Using self
{: #ex-6-1-2 }

This class converts a Celsius reading to Fahrenheit.

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return celsius * 9 / 5 + 32

reading = Temperature(100)
print(reading.to_fahrenheit())   # 212.0
```

[Solution 6.1.2]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-1-2) &middot; [`ex_6_1_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_1_2.py)

### Exercise 6.1.3 — Storing an attribute
{: #ex-6-1-3 }

This class records a student's name and quiz score, then prints a summary.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def summary(self):
        return f"{self.name} scored {self.grade}"

learner = Student("Ava", 88)
print(learner.summary())   # Ava scored 88
```

[Solution 6.1.3]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-1-3) &middot; [`ex_6_1_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_1_3.py)

### Exercise 6.1.4 — Calling a method
{: #ex-6-1-4 }

This class models a savings account and adds interest to the balance.

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def add_interest(self, rate):
        self.balance = self.balance + self.balance * rate

savings = Account(1000)
Account.add_interest(0.05)
print(savings.balance)   # 1050.0
```

[Solution 6.1.4]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-1-4) &middot; [`ex_6_1_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_1_4.py)

### Exercise 6.1.5 — Method calls need parentheses
{: #ex-6-1-5 }

This class stores a circle's radius and returns its circumference.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius

wheel = Circle(10)
print(wheel.circumference)   # 62.8318
```

[Solution 6.1.5]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-1-5) &middot; [`ex_6_1_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_1_5.py)

## Exercises 6.2.1–6.2.5

### Exercise 6.2.1 — Instance vs class attribute
{: #ex-6-2-1 }

Every planet shares the same gravity unit, but each has its own mass. This program should print each planet's name and the shared unit.

```python
class Planet:
    gravity_unit = "m/s^2"

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

earth = Planet("Earth", 5.97e24)
mars = Planet("Mars", 6.42e23)

print(earth.name, earth.gravity_unit)   # Earth m/s^2
print(mars.name, mars.gravity_unit)     # Mars m/s^2
print(earth.unit)                       # m/s^2
```

[Solution 6.2.1]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-2-1) &middot; [`ex_6_2_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_2_1.py)

### Exercise 6.2.2 — Shared mutable class attribute
{: #ex-6-2-2 }

Each runner should keep a private list of lap times, but every runner ends up sharing one list.

```python
class Runner:
    laps = []

    def __init__(self, name):
        self.name = name

    def record(self, seconds):
        self.laps.append(seconds)

amir = Runner("Amir")
beth = Runner("Beth")
amir.record(58)
beth.record(61)
print(amir.laps)   # [58]
print(beth.laps)   # [61]
```

[Solution 6.2.2]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-2-2) &middot; [`ex_6_2_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_2_2.py)

### Exercise 6.2.3 — Updating a class counter
{: #ex-6-2-3 }

A class attribute should count how many books have been created.

```python
class Book:
    count = 0

    def __init__(self, title):
        self.title = title
        self.count = self.count + 1

Book("Algebra")
Book("Biology")
Book("Chemistry")
print(Book.count)   # 3
```

[Solution 6.2.3]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-2-3) &middot; [`ex_6_2_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_2_3.py)

### Exercise 6.2.4 — Instance overriding shared default
{: #ex-6-2-4 }

Every thermostat shares a default target, but the kitchen is set warmer for itself only. The bedroom should keep the shared default.

```python
class Thermostat:
    target_c = 20

    def __init__(self, room):
        self.room = room

kitchen = Thermostat("kitchen")
bedroom = Thermostat("bedroom")
Thermostat.target_c = 22

print(kitchen.target_c)   # 22
print(bedroom.target_c)   # 20
```

[Solution 6.2.4]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-2-4) &middot; [`ex_6_2_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_2_4.py)

### Exercise 6.2.5 — Reading a class constant
{: #ex-6-2-5 }

The class stores a fixed sales-tax rate shared by all carts; each cart has its own subtotal. The total should add the tax.

```python
class Cart:
    tax_rate = 0.08

    def __init__(self, subtotal):
        self.subtotal = subtotal

    def total(self):
        return self.subtotal + self.subtotal / self.tax_rate

groceries = Cart(50.0)
print(groceries.total())   # 54.0
```

[Solution 6.2.5]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-2-5) &middot; [`ex_6_2_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_2_5.py)

## Exercises 6.3.1–6.3.5

### Exercise 6.3.1 — Relying on a shared method
{: #ex-6-3-1 }

Different shapes each provide an `area()` method, so one function can total them all.

```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

def total_area(shapes):
    total = 0
    for shape in shapes:
        total = total + shape.area
    return total

print(total_area([Square(4), Triangle(6, 3)]))   # 25.0
```

[Solution 6.3.1]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-3-1) &middot; [`ex_6_3_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_3_1.py)

### Exercise 6.3.2 — Same behavior, different types
{: #ex-6-3-2 }

Any object that can `speak()` can be greeted, regardless of its class.

```python
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
```

[Solution 6.3.2]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-3-2) &middot; [`ex_6_3_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_3_2.py)

### Exercise 6.3.3 — Behavior over type
{: #ex-6-3-3 }

A function should work with anything that has a `length` attribute.

```python
class Field:
    def __init__(self, length):
        self.length = length

class Pool:
    def __init__(self, length):
        self.length = length

def meters_of(thing):
    return thing.size

print(meters_of(Field(100)))   # 100
print(meters_of(Pool(25)))     # 25
```

[Solution 6.3.3]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-3-3) &middot; [`ex_6_3_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_3_3.py)

### Exercise 6.3.4 — Duck typing a method call
{: #ex-6-3-4 }

Different timers each provide `tick()`, so one loop can advance them all.

```python
class Stopwatch:
    def __init__(self):
        self.seconds = 0

    def tick(self):
        self.seconds = self.seconds + 1

class Metronome:
    def __init__(self):
        self.beats = 0

    def tick(self):
        self.beats = self.beats + 1

def advance(devices):
    for device in devices:
        device.tick

watch = Stopwatch()
advance([watch])
print(watch.seconds)   # 1
```

[Solution 6.3.4]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-3-4) &middot; [`ex_6_3_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_3_4.py)

### Exercise 6.3.5 — Trusting the interface
{: #ex-6-3-5 }

Any sensor that provides a `read()` method can be sampled.

```python
class TempSensor:
    def read(self):
        return 21.5

class HumiditySensor:
    def read(self):
        return 48.0

def sample(sensor):
    return sensor.read

print(sample(TempSensor()))       # 21.5
print(sample(HumiditySensor()))   # 48.0
```

[Solution 6.3.5]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-3-5) &middot; [`ex_6_3_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_3_5.py)

## Exercises 6.4.1–6.4.5

### Exercise 6.4.1 — A list is mutable
{: #ex-6-4-1 }

This program corrects a typo in a list of daily temperatures.

```python
tokyo_temps = [33.0, 36.5, 31.0]
tokyo_temps[3] = 33.5
print(tokyo_temps)   # [33.5, 36.5, 31.0]
```

[Solution 6.4.1]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-4-1) &middot; [`ex_6_4_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_4_1.py)

### Exercise 6.4.2 — Aliasing a list
{: #ex-6-4-2 }

The two names are meant to refer to the same list, so a change through one is seen through the other. This should print the list with the new reading.

```python
readings = [12, 15, 9]
same_readings = list(readings)
same_readings.append(20)
print(readings)   # [12, 15, 9, 20]
```

[Solution 6.4.2]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-4-2) &middot; [`ex_6_4_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_4_2.py)

### Exercise 6.4.3 — Appending to a list
{: #ex-6-4-3 }

This program builds a list of square numbers from 1 to 5.

```python
squares = []
for n in range(1, 6):
    squares.append(n + n)
print(squares)   # [1, 4, 9, 16, 25]
```

[Solution 6.4.3]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-4-3) &middot; [`ex_6_4_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_4_3.py)

### Exercise 6.4.4 — Indexing the last item
{: #ex-6-4-4 }

This program prints the most recent score in the list.

```python
scores = [91, 87, 95, 78]
latest = scores[len(scores)]
print(latest)   # 78
```

[Solution 6.4.4]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-4-4) &middot; [`ex_6_4_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_4_4.py)

### Exercise 6.4.5 — A list method
{: #ex-6-4-5 }

This program removes a finished task from the to-do list.

```python
tasks = ["email", "report", "lunch"]
tasks.remove(1)
print(tasks)   # ['email', 'lunch']
```

[Solution 6.4.5]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-4-5) &middot; [`ex_6_4_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_4_5.py)

## Exercises 6.5.1–6.5.5

### Exercise 6.5.1 — Assignment is not a copy
{: #ex-6-5-1 }

The backup should stay unchanged after we add a new reading to the original.

```python
temps = [33.0, 36.5, 31.0]
backup = temps
temps.append(34.0)
print(backup)   # [33.0, 36.5, 31.0]
```

[Solution 6.5.1]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-5-1) &middot; [`ex_6_5_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_5_1.py)

### Exercise 6.5.2 — Making a shallow copy
{: #ex-6-5-2 }

This should make an independent copy of a flat list of prices.

```python
prices = [1.99, 2.49, 0.99]
copy_of_prices = prices.copy
copy_of_prices.append(5.00)
print(prices)            # [1.99, 2.49, 0.99]
print(copy_of_prices)    # [1.99, 2.49, 0.99, 5.0]
```

[Solution 6.5.2]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-5-2) &middot; [`ex_6_5_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_5_2.py)

### Exercise 6.5.3 — Copying with a slice
{: #ex-6-5-3 }

A slice copy of a flat list should leave the original alone.

```python
grades = [85, 90, 78]
working = grades[0:2]
working.append(100)
print(grades)    # [85, 90, 78]
print(working)   # [85, 90, 78, 100]
```

[Solution 6.5.3]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-5-3) &middot; [`ex_6_5_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_5_3.py)

### Exercise 6.5.4 — Deep copy for nested lists
{: #ex-6-5-4 }

The grid holds rows of numbers. We want an independent copy whose rows can change without touching the original.

```python
import copy

grid = [[1, 2], [3, 4]]
independent = copy.copy(grid)
independent[0].append(99)
print(grid)         # [[1, 2], [3, 4]]
print(independent)  # [[1, 2, 99], [3, 4]]
```

[Solution 6.5.4]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-5-4) &middot; [`ex_6_5_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_5_4.py)

### Exercise 6.5.5 — Shallow copy shares inner lists
{: #ex-6-5-5 }

The seating chart is a list of rows. We copy it, then add a seat to one row of the copy; the original chart should be unchanged.

```python
import copy

seats = [["A1", "A2"], ["B1", "B2"]]
new_seats = seats.copy()
new_seats[0].append("A3")
print(seats)       # [['A1', 'A2'], ['B1', 'B2']]
print(new_seats)   # [['A1', 'A2', 'A3'], ['B1', 'B2']]
```

[Solution 6.5.5]({{ site.baseurl }}/ep/solutions/06-objects/#sol-6-5-5) &middot; [`ex_6_5_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_6_5_5.py)

