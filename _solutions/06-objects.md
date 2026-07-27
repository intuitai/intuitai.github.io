---
title: "Chapter 6: Objects — Solutions"
short_title: "Ch. 6 — Objects"
layout: post
permalink: /ep/solutions/06-objects/
order: 2
chapter: 6
---

Worked solutions to the 25 *Find the Bug* exercises in [Chapter 6: Objects]({{ site.baseurl }}/ep/exercises/06-objects/). Each one names the kind of bug, explains why the original misbehaved, and shows the corrected program.

Solutions stay folded until you open them — try the exercise first; the diagnosis is where the learning is.

## Solutions 6.1.1–6.1.5

### Solution 6.1.1 — Defining a class
{: #sol-6-1-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `def __init__(self, width, height)` header is missing the colon at the end, so Python cannot parse the method definition. Adding the colon fixes it.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

room = Rectangle(4, 3)
print(room.area())   # 12
```

[Back to Exercise 6.1.1]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-1-1) &middot; [`sol_6_1_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_1_1.py)

</details>

### Solution 6.1.2 — Using self
{: #sol-6-1-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Inside `to_fahrenheit` the bare name `celsius` is not defined; the value is stored on the instance, so it must be reached through `self“.celsius`. Using `self.celsius` fixes the `NameError`.

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

reading = Temperature(100)
print(reading.to_fahrenheit())   # 212.0
```

[Back to Exercise 6.1.2]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-1-2) &middot; [`sol_6_1_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_1_2.py)

</details>

### Solution 6.1.3 — Storing an attribute
{: #sol-6-1-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The attribute stored in `__init__` is named `score`, but `summary` reads `self.grade`, which was never set. Referring to `self.score` fixes the `AttributeError`.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def summary(self):
        return f"{self.name} scored {self.score}"

learner = Student("Ava", 88)
print(learner.summary())   # Ava scored 88
```

[Back to Exercise 6.1.3]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-1-3) &middot; [`sol_6_1_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_1_3.py)

</details>

### Solution 6.1.4 — Calling a method
{: #sol-6-1-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The method is called on the class, `Account.add_interest(0.05)`, so `0.05` is bound to `self` and no `rate` is supplied, raising a `TypeError`. Calling it on the instance, `savings.add_interest(0.05)`, passes `savings` as `self` and `0.05` as `rate`.

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def add_interest(self, rate):
        self.balance = self.balance + self.balance * rate

savings = Account(1000)
savings.add_interest(0.05)
print(savings.balance)   # 1050.0
```

[Back to Exercise 6.1.4]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-1-4) &middot; [`sol_6_1_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_1_4.py)

</details>

### Solution 6.1.5 — Method calls need parentheses
{: #sol-6-1-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`wheel.circumference` refers to the method object instead of calling it, so the printout is a function reference, not the number. Adding parentheses — `wheel.circumference()` — calls the method and prints `62.8318`.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius

wheel = Circle(10)
print(wheel.circumference())   # 62.8318
```

[Back to Exercise 6.1.5]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-1-5) &middot; [`sol_6_1_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_1_5.py)

</details>

## Solutions 6.2.1–6.2.5

### Solution 6.2.1 — Instance vs class attribute
{: #sol-6-2-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The class attribute is named `gravity_unit`, but the last line reads `earth.unit`, which does not exist. Using `earth.gravity_unit` fixes the `AttributeError`.

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
print(earth.gravity_unit)               # m/s^2
```

[Back to Exercise 6.2.1]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-2-1) &middot; [`sol_6_2_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_2_1.py)

</details>

### Solution 6.2.2 — Shared mutable class attribute
{: #sol-6-2-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`laps` is a class attribute, so a single list is shared by every runner; `amir.record` and `beth.record` append to the same list. Each runner needs its own list, created as an instance attribute in `__init__`.

```python
class Runner:
    def __init__(self, name):
        self.name = name
        self.laps = []

    def record(self, seconds):
        self.laps.append(seconds)

amir = Runner("Amir")
beth = Runner("Beth")
amir.record(58)
beth.record(61)
print(amir.laps)   # [58]
print(beth.laps)   # [61]
```

[Back to Exercise 6.2.2]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-2-2) &middot; [`sol_6_2_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_2_2.py)

</details>

### Solution 6.2.3 — Updating a class counter
{: #sol-6-2-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Writing `self.count = self.count + 1` reads the class value but creates a new *instance* attribute, leaving `Book.count` at 0. Incrementing `Book.count` updates the shared class counter, so it reaches 3.

```python
class Book:
    count = 0

    def __init__(self, title):
        self.title = title
        Book.count = Book.count + 1

Book("Algebra")
Book("Biology")
Book("Chemistry")
print(Book.count)   # 3
```

[Back to Exercise 6.2.3]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-2-3) &middot; [`sol_6_2_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_2_3.py)

</details>

### Solution 6.2.4 — Instance overriding shared default
{: #sol-6-2-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`Thermostat.target_c = 22` reassigns the shared *class* attribute, so both rooms read 22 and the bedroom does not keep the default. Assigning to the instance, `kitchen.target_c = 22`, creates an instance attribute that shadows the class default for the kitchen only, leaving the bedroom at 20.

```python
class Thermostat:
    target_c = 20

    def __init__(self, room):
        self.room = room

kitchen = Thermostat("kitchen")
bedroom = Thermostat("bedroom")
kitchen.target_c = 22   # set only this instance

print(kitchen.target_c)   # 22
print(bedroom.target_c)   # 20
```

[Back to Exercise 6.2.4]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-2-4) &middot; [`sol_6_2_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_2_4.py)

</details>

### Solution 6.2.5 — Reading a class constant
{: #sol-6-2-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Sales tax is added by *multiplying* the subtotal by the rate, not dividing by it. The corrected line uses `self.subtotal + self.subtotal * self.tax_rate`, giving `54.0`.

```python
class Cart:
    tax_rate = 0.08

    def __init__(self, subtotal):
        self.subtotal = subtotal

    def total(self):
        return self.subtotal + self.subtotal * self.tax_rate

groceries = Cart(50.0)
print(groceries.total())   # 54.0
```

[Back to Exercise 6.2.5]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-2-5) &middot; [`sol_6_2_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_2_5.py)

</details>

## Solutions 6.3.1–6.3.5

### Solution 6.3.1 — Relying on a shared method
{: #sol-6-3-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`shape.area` refers to the method without calling it, so adding it to a number raises a `TypeError`. Calling `shape.area()` invokes each shape's method and totals the areas to `25.0`.

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
        total = total + shape.area()
    return total

print(total_area([Square(4), Triangle(6, 3)]))   # 25.0
```

[Back to Exercise 6.3.1]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-3-1) &middot; [`sol_6_3_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_3_1.py)

</details>

### Solution 6.3.2 — Same behavior, different types
{: #sol-6-3-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`greet` calls `animal.speka()`, but both classes provide `speak`, not `speka`, so every call raises an `AttributeError`. Correcting the method name to `animal.speak()` lets duck typing work for any object that can `speak`.

```python
class Cat:
    def speak(self):
        return "Meow"

class Cow:
    def speak(self):
        return "Moo"

def greet(animal):
    print("The animal says:", animal.speak())

greet(Cat())
greet(Cow())   # The animal says: Moo
```

[Back to Exercise 6.3.2]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-3-2) &middot; [`sol_6_3_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_3_2.py)

</details>

### Solution 6.3.3 — Behavior over type
{: #sol-6-3-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Both objects expose a `length` attribute, but `meters_of` reads `thing.size`, which neither class has. Reading `thing.length` fixes the `AttributeError`, and any object with a `length` works.

```python
class Field:
    def __init__(self, length):
        self.length = length

class Pool:
    def __init__(self, length):
        self.length = length

def meters_of(thing):
    return thing.length

print(meters_of(Field(100)))   # 100
print(meters_of(Pool(25)))     # 25
```

[Back to Exercise 6.3.3]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-3-3) &middot; [`sol_6_3_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_3_3.py)

</details>

### Solution 6.3.4 — Duck typing a method call
{: #sol-6-3-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`device.tick` only looks up the method; it never calls it, so `watch.seconds` stays 0. Adding parentheses — `device.tick()` — actually advances each device.

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
        device.tick()

watch = Stopwatch()
advance([watch])
print(watch.seconds)   # 1
```

[Back to Exercise 6.3.4]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-3-4) &middot; [`sol_6_3_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_3_4.py)

</details>

### Solution 6.3.5 — Trusting the interface
{: #sol-6-3-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`sensor.read` returns the bound method instead of the reading, so the printout is a method reference, not a number. Calling `sensor.read()` returns the value from whichever sensor was passed.

```python
class TempSensor:
    def read(self):
        return 21.5

class HumiditySensor:
    def read(self):
        return 48.0

def sample(sensor):
    return sensor.read()

print(sample(TempSensor()))       # 21.5
print(sample(HumiditySensor()))   # 48.0
```

[Back to Exercise 6.3.5]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-3-5) &middot; [`sol_6_3_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_3_5.py)

</details>

## Solutions 6.4.1–6.4.5

### Solution 6.4.1 — A list is mutable
{: #sol-6-4-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The list has three items at indexes 0, 1, and 2, so `tokyo_temps[3]` is out of range and raises an `IndexError`. The typo is at index 0, so the fix assigns to `tokyo_temps[0]`.

```python
tokyo_temps = [33.0, 36.5, 31.0]
tokyo_temps[0] = 33.5
print(tokyo_temps)   # [33.5, 36.5, 31.0]
```

[Back to Exercise 6.4.1]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-4-1) &middot; [`sol_6_4_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_4_1.py)

</details>

### Solution 6.4.2 — Aliasing a list
{: #sol-6-4-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`list(readings)` builds a brand-new list, so `same_readings` is a separate object and appending to it does not change `readings`. To make both names refer to the same list, assign directly with `same_readings = readings`.

```python
readings = [12, 15, 9]
same_readings = readings
same_readings.append(20)
print(readings)   # [12, 15, 9, 20]
```

[Back to Exercise 6.4.2]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-4-2) &middot; [`sol_6_4_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_4_2.py)

</details>

### Solution 6.4.3 — Appending to a list
{: #sol-6-4-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`n + n` doubles each number instead of squaring it, so the list comes out `[2, 4, 6, 8, 10]`. Squaring with `n * n` (or `n ** 2`) produces the intended `[1, 4, 9, 16, 25]`.

```python
squares = []
for n in range(1, 6):
    squares.append(n * n)
print(squares)   # [1, 4, 9, 16, 25]
```

[Back to Exercise 6.4.3]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-4-3) &middot; [`sol_6_4_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_4_3.py)

</details>

### Solution 6.4.4 — Indexing the last item
{: #sol-6-4-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`len(scores)` is 4, but valid indexes are 0 through 3, so `scores[len(scores)]` raises an `IndexError`. The last item is at `scores[len(scores) - 1]`, or more simply `scores[-1]`.

```python
scores = [91, 87, 95, 78]
latest = scores[-1]
print(latest)   # 78
```

[Back to Exercise 6.4.4]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-4-4) &middot; [`sol_6_4_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_4_4.py)

</details>

### Solution 6.4.5 — A list method
{: #sol-6-4-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`list.remove` deletes by *value*, not by index, so `tasks.remove(1)` looks for the value `1` and raises a `ValueError`. To drop the finished task by value, remove `"report"` (or use `del tasks[1]`).

```python
tasks = ["email", "report", "lunch"]
tasks.remove("report")
print(tasks)   # ['email', 'lunch']
```

[Back to Exercise 6.4.5]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-4-5) &middot; [`sol_6_4_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_4_5.py)

</details>

## Solutions 6.5.1–6.5.5

### Solution 6.5.1 — Assignment is not a copy
{: #sol-6-5-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`backup = temps` makes both names point at the same list, so appending to `temps` also changes `backup`. Taking a real copy with `temps.copy()` (or `temps[:]`) keeps the backup unchanged.

```python
temps = [33.0, 36.5, 31.0]
backup = temps.copy()
temps.append(34.0)
print(backup)   # [33.0, 36.5, 31.0]
```

[Back to Exercise 6.5.1]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-5-1) &middot; [`sol_6_5_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_5_1.py)

</details>

### Solution 6.5.2 — Making a shallow copy
{: #sol-6-5-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`prices.copy` refers to the method without calling it, so `copy_of_prices` becomes a method object and `.append` raises an `AttributeError`. Calling `prices.copy()` makes the independent copy.

```python
prices = [1.99, 2.49, 0.99]
copy_of_prices = prices.copy()
copy_of_prices.append(5.00)
print(prices)            # [1.99, 2.49, 0.99]
print(copy_of_prices)    # [1.99, 2.49, 0.99, 5.0]
```

[Back to Exercise 6.5.2]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-5-2) &middot; [`sol_6_5_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_5_2.py)

</details>

### Solution 6.5.3 — Copying with a slice
{: #sol-6-5-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The slice `grades[0:2]` copies only the first two items, so `working` starts as `[85, 90]` and the result is wrong. A full-list slice `grades[:]` copies every element.

```python
grades = [85, 90, 78]
working = grades[:]
working.append(100)
print(grades)    # [85, 90, 78]
print(working)   # [85, 90, 78, 100]
```

[Back to Exercise 6.5.3]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-5-3) &middot; [`sol_6_5_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_5_3.py)

</details>

### Solution 6.5.4 — Deep copy for nested lists
{: #sol-6-5-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`copy.copy` makes a shallow copy, so the inner lists are still shared and appending to `independent[0]` also changes `grid`. `copy.deepcopy` copies the nested lists recursively, keeping the original intact.

```python
import copy

grid = [[1, 2], [3, 4]]
independent = copy.deepcopy(grid)
independent[0].append(99)
print(grid)         # [[1, 2], [3, 4]]
print(independent)  # [[1, 2, 99], [3, 4]]
```

[Back to Exercise 6.5.4]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-5-4) &middot; [`sol_6_5_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_5_4.py)

</details>

### Solution 6.5.5 — Shallow copy shares inner lists
{: #sol-6-5-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`seats.copy()` is a shallow copy: the outer list is new, but the row lists are shared, so `new_seats[0].append` also changes `seats`. Using `copy.deepcopy` copies each row, leaving the original chart unchanged.

```python
import copy

seats = [["A1", "A2"], ["B1", "B2"]]
new_seats = copy.deepcopy(seats)
new_seats[0].append("A3")
print(seats)       # [['A1', 'A2'], ['B1', 'B2']]
print(new_seats)   # [['A1', 'A2', 'A3'], ['B1', 'B2']]
```

[Back to Exercise 6.5.5]({{ site.baseurl }}/ep/exercises/06-objects/#ex-6-5-5) &middot; [`sol_6_5_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_6_5_5.py)

</details>

