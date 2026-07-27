---
title: "Chapter 10: Functions"
short_title: "Ch. 10 — Functions"
layout: post
permalink: /ep/exercises/10-functions/
order: 6
chapter: 10
exercise_count: 60
---

60 *Find the Bug* exercises from Chapter 10 of *Everyday Programming*. Every program below is short, does something recognizable, and hides **exactly one** bug — syntax, runtime, or logical. Read it, predict what it does, then run it and find out.

Worked solutions for this chapter: [Chapter 10 solutions]({{ site.baseurl }}/ep/solutions/10-functions/). Every snippet is also available as a `.py` file — see [Exercises &amp; Solutions]({{ site.baseurl }}/ep/book/exercises/).

## Exercises 10.1.1–10.1.5

### Exercise 10.1.1 — Defining and calling
{: #ex-10-1-1 }

This program should define a function that prints a welcome message and then call it once.

```python
def welcome():
    print("Welcome to the science club!")

welcome
```

[Solution 10.1.1]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-1-1) &middot; [`ex_10_1_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_1_1.py)

### Exercise 10.1.2 — The colon
{: #ex-10-1-2 }

This program defines a function that prints the boiling point of water and calls it.

```python
def boiling_point()
    print("Water boils at 100 degrees Celsius.")

boiling_point()
```

[Solution 10.1.2]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-1-2) &middot; [`ex_10_1_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_1_2.py)

### Exercise 10.1.3 — The function body
{: #ex-10-1-3 }

This program should print the number of days in a week when called.

```python
def days_in_week():
print("A week has 7 days.")

days_in_week()
```

[Solution 10.1.3]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-1-3) &middot; [`ex_10_1_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_1_3.py)

### Exercise 10.1.4 — Indenting the body
{: #ex-10-1-4 }

This program defines a function with two body lines and calls it once.

```python
def study_plan():
    print("Read the chapter.")
  print("Solve five problems.")

study_plan()
```

[Solution 10.1.4]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-1-4) &middot; [`ex_10_1_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_1_4.py)

### Exercise 10.1.5 — Remember to call
{: #ex-10-1-5 }

This program should actually print the freezing point of water on screen.

```python
def freezing_point():
    print("Water freezes at 0 degrees Celsius.")
```

[Solution 10.1.5]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-1-5) &middot; [`ex_10_1_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_1_5.py)

## Exercises 10.2.1–10.2.5

### Exercise 10.2.1 — Passing an argument
{: #ex-10-2-1 }

This program should greet a student by name.

```python
def greet_student(name):
    print("Hello,", name)

greet_student()
```

[Solution 10.2.1]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-2-1) &middot; [`ex_10_2_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_2_1.py)

### Exercise 10.2.2 — Parameter order
{: #ex-10-2-2 }

This program should print `"Maya is 15 years old"`.

```python
def describe(name, age):
    print(name, "is", age, "years old")

describe(15, "Maya")
```

[Solution 10.2.2]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-2-2) &middot; [`ex_10_2_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_2_2.py)

### Exercise 10.2.3 — Too many arguments
{: #ex-10-2-3 }

This program should print the area of a rectangle that is 4 by 6.

```python
def rectangle_area(width, height):
    return width * height

print(rectangle_area(4, 6, 8))
```

[Solution 10.2.3]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-2-3) &middot; [`ex_10_2_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_2_3.py)

### Exercise 10.2.4 — Using the parameter
{: #ex-10-2-4 }

This program should double the number that is passed in and print 10.

```python
def double(number):
    return number * 2

print(double(number))
```

[Solution 10.2.4]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-2-4) &middot; [`ex_10_2_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_2_4.py)

### Exercise 10.2.5 — Two parameters
{: #ex-10-2-5 }

This program should compute the perimeter of a rectangle (2 times width plus 2 times height) for a 3 by 5 rectangle, giving 16.

```python
def perimeter(width, height):
    return 2 * width + 2 * width

print(perimeter(3, 5))  # 16
```

[Solution 10.2.5]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-2-5) &middot; [`ex_10_2_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_2_5.py)

## Exercises 10.3.1–10.3.5

### Exercise 10.3.1 — Return, do not print
{: #ex-10-3-1 }

This program should store the sum of two numbers and then print 12.

```python
def add(a, b):
    print(a + b)

total = add(5, 7)
print(total)  # 12
```

[Solution 10.3.1]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-3-1) &middot; [`ex_10_3_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_3_1.py)

### Exercise 10.3.2 — Return the right value
{: #ex-10-3-2 }

This function should return the average of three test scores.

```python
def average_of_three(a, b, c):
    return a + b + c / 3

print(average_of_three(80, 90, 100))  # 90.0
```

[Solution 10.3.2]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-3-2) &middot; [`ex_10_3_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_3_2.py)

### Exercise 10.3.3 — Returning early
{: #ex-10-3-3 }

This program should convert Celsius to Fahrenheit and print 212.0 for 100 degrees.

```python
def c_to_f(celsius):
    return
    celsius * 9 / 5 + 32

print(c_to_f(100))  # 212.0
```

[Solution 10.3.3]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-3-3) &middot; [`ex_10_3_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_3_3.py)

### Exercise 10.3.4 — Return what was asked
{: #ex-10-3-4 }

This function should return the larger of two numbers; here it should return 9.

```python
def larger(a, b):
    if a > b:
        return a
    else:
        return a

print(larger(4, 9))  # 9
```

[Solution 10.3.4]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-3-4) &middot; [`ex_10_3_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_3_4.py)

### Exercise 10.3.5 — Use the returned value
{: #ex-10-3-5 }

This program should print the square of 6, which is 36.

```python
def square(side):
    return side * side

square(6)
print(area)  # 36
```

[Solution 10.3.5]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-3-5) &middot; [`ex_10_3_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_3_5.py)

## Exercises 10.4.1–10.4.5

### Exercise 10.4.1 — A default value
{: #ex-10-4-1 }

This program should print a greeting with the default name when called with no argument.

```python
def greet(name="friend"):
    print("Hello,", name)

greet
```

[Solution 10.4.1]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-4-1) &middot; [`ex_10_4_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_4_1.py)

### Exercise 10.4.2 — Default tax rate
{: #ex-10-4-2 }

This function should add an 8 percent tax by default, so a 50 dollar bill becomes 54.0.

```python
def with_tax(price, rate=0.08):
    return price + price * 0.8

print(with_tax(50))  # 54.0
```

[Solution 10.4.2]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-4-2) &middot; [`ex_10_4_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_4_2.py)

### Exercise 10.4.3 — Overriding the default
{: #ex-10-4-3 }

This program should print 200 by overriding the default step count.

```python
def total_steps(days, per_day=100):
    return days * per_day

print(total_steps(2, 200))  # 200
```

[Solution 10.4.3]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-4-3) &middot; [`ex_10_4_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_4_3.py)

### Exercise 10.4.4 — Order of defaults
{: #ex-10-4-4 }

This function gives the area of a rectangle, using a default height of 1.

```python
def area(height=1, width):
    return width * height

print(area(width=5))  # 5
```

[Solution 10.4.4]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-4-4) &middot; [`ex_10_4_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_4_4.py)

### Exercise 10.4.5 — The default is optional
{: #ex-10-4-5 }

This program should print 10 by relying on the default increment.

```python
def increase(value, by=10):
    return value + by

print(increase())  # 10
```

[Solution 10.4.5]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-4-5) &middot; [`ex_10_4_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_4_5.py)

## Exercises 10.5.1–10.5.5

### Exercise 10.5.1 — Calling by name
{: #ex-10-5-1 }

This program should print `"Lina is 12 years old"` using keyword arguments.

```python
def introduce(name, age):
    print(name, "is", age, "years old")

introduce(name="Lina", age=12, grade=7)
```

[Solution 10.5.1]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-5-1) &middot; [`ex_10_5_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_5_1.py)

### Exercise 10.5.2 — Order independence
{: #ex-10-5-2 }

Keyword arguments let you reorder; this should print the speed as distance over time, 20.0.

```python
def speed(distance, time):
    return distance / time

print(speed(time=100, distance=5))  # 20.0
```

[Solution 10.5.2]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-5-2) &middot; [`ex_10_5_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_5_2.py)

### Exercise 10.5.3 — Spelling the keyword
{: #ex-10-5-3 }

This program should print a labeled temperature using a keyword argument.

```python
def report(city, temperature):
    print(city, "is at", temperature, "degrees")

report(city="Denver", temp=30)
```

[Solution 10.5.3]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-5-3) &middot; [`ex_10_5_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_5_3.py)

### Exercise 10.5.4 — Keyword after positional
{: #ex-10-5-4 }

This program should print `"Sam scored 95"` using one positional and one keyword argument.

```python
def score_line(name, points):
    print(name, "scored", points)

score_line(name="Sam", 95)
```

[Solution 10.5.4]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-5-4) &middot; [`ex_10_5_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_5_4.py)

### Exercise 10.5.5 — Mixing names and positions
{: #ex-10-5-5 }

This should compute simple interest (principal times rate times years) as 60.0.

```python
def interest(principal, rate, years):
    return principal * rate * years

print(interest(1000, years=3, rate=0.02, time=3))  # 60.0
```

[Solution 10.5.5]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-5-5) &middot; [`ex_10_5_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_5_5.py)

## Exercises 10.6.1–10.6.5

### Exercise 10.6.1 — Returning a pair
{: #ex-10-6-1 }

This program should print the smallest and largest of three temperatures.

```python
def min_max(a, b, c):
    return min(a, b, c)

low, high = min_max(31.0, 36.5, 33.0)
print(low, high)  # 31.0 36.5
```

[Solution 10.6.1]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-6-1) &middot; [`ex_10_6_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_6_1.py)

### Exercise 10.6.2 — Unpacking the result
{: #ex-10-6-2 }

This program should print the quotient and remainder of 17 divided by 5.

```python
def divide(a, b):
    return a // b, a % b

quotient = divide(17, 5)
print(quotient, remainder)  # 3 2
```

[Solution 10.6.2]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-6-2) &middot; [`ex_10_6_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_6_2.py)

### Exercise 10.6.3 — Matching the count
{: #ex-10-6-3 }

This program should unpack a name and an age into two variables.

```python
def person():
    return "Luis", 14, "grade 8"

name, age = person()
print(name, age)  # Luis 14
```

[Solution 10.6.3]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-6-3) &middot; [`ex_10_6_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_6_3.py)

### Exercise 10.6.4 — Order of the tuple
{: #ex-10-6-4 }

This should report width then height of a 8 by 3 rectangle, printing `"width 8 height 3"`.

```python
def dimensions():
    return 3, 8

width, height = dimensions()
print("width", width, "height", height)
```

[Solution 10.6.4]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-6-4) &middot; [`ex_10_6_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_6_4.py)

### Exercise 10.6.5 — Returning both values
{: #ex-10-6-5 }

This program should return and print both the sum and the product of 4 and 5.

```python
def sum_and_product(a, b):
    return a + b
    return a * b

total, product = sum_and_product(4, 5)
print(total, product)  # 9 20
```

[Solution 10.6.5]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-6-5) &middot; [`ex_10_6_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_6_5.py)

## Exercises 10.7.1–10.7.5

### Exercise 10.7.1 — No return means None
{: #ex-10-7-1 }

This program prints a message, and the returned value should be `None`.

```python
def announce():
    print("The meeting starts now.")
    return "done"

result = announce()
print(result)  # None
```

[Solution 10.7.1]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-7-1) &middot; [`ex_10_7_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_7_1.py)

### Exercise 10.7.2 — Forgetting to return
{: #ex-10-7-2 }

This program should print the doubled value 14, using the function's return value.

```python
def double(number):
    answer = number * 2

print(double(7))  # 14
```

[Solution 10.7.2]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-7-2) &middot; [`ex_10_7_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_7_2.py)

### Exercise 10.7.3 — Printing is not returning
{: #ex-10-7-3 }

This should store the area of a circle approximation and print about 78.5, then use it again.

```python
def circle_area(radius):
    print(3.14 * radius * radius)

area = circle_area(5)
print(area * 2)  # uses the area twice
```

[Solution 10.7.3]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-7-3) &middot; [`ex_10_7_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_7_3.py)

### Exercise 10.7.4 — None in arithmetic
{: #ex-10-7-4 }

This program should add 5 to the result of a function that returns a number.

```python
def base_value():
    total = 10

print(base_value() + 5)  # 15
```

[Solution 10.7.4]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-7-4) &middot; [`ex_10_7_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_7_4.py)

### Exercise 10.7.5 — Expecting a value
{: #ex-10-7-5 }

This should check whether the helper returned a usable number and print it; it should print 42.

```python
def lucky_number():
    chosen = 42

number = lucky_number()
print(number)  # 42
```

[Solution 10.7.5]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-7-5) &middot; [`ex_10_7_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_7_5.py)

## Exercises 10.8.1–10.8.5

### Exercise 10.8.1 — Triple quotes
{: #ex-10-8-1 }

This function has a docstring describing what it does.

```python
def add(a, b):
    "Return the sum of two numbers.'''
    return a + b

print(add(2, 3))  # 5
```

[Solution 10.8.1]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-8-1) &middot; [`ex_10_8_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_8_1.py)

### Exercise 10.8.2 — Docstring placement
{: #ex-10-8-2 }

The docstring should sit directly under the `def` line so it becomes the function's documentation.

```python
def to_meters(feet):
    result = feet * 0.3048
    """Convert feet to meters."""
    return result

print(to_meters.__doc__)  # Convert feet to meters.
```

[Solution 10.8.2]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-8-2) &middot; [`ex_10_8_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_8_2.py)

### Exercise 10.8.3 — Reading the docstring
{: #ex-10-8-3 }

This program should print the docstring of the function.

```python
def half(number):
    """Return half of a number."""
    return number / 2

print(half.__docs__)
```

[Solution 10.8.3]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-8-3) &middot; [`ex_10_8_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_8_3.py)

### Exercise 10.8.4 — Closing the quotes
{: #ex-10-8-4 }

This function should have a one-line docstring and return a perimeter.

```python
def square_perimeter(side):
    """Return the perimeter of a square.
    return side * 4

print(square_perimeter(3))  # 12
```

[Solution 10.8.4]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-8-4) &middot; [`ex_10_8_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_8_4.py)

### Exercise 10.8.5 — Docstring, then code
{: #ex-10-8-5 }

This program should print the function's docstring.

```python
def kelvin(celsius):
    """Convert Celsius to Kelvin.
    return celsius + 273.15

print(kelvin.__doc__)
```

[Solution 10.8.5]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-8-5) &middot; [`ex_10_8_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_8_5.py)

## Exercises 10.9.1–10.9.5

### Exercise 10.9.1 — Collecting positionals
{: #ex-10-9-1 }

This program should sum any number of grades passed in; here the total should be 270.

```python
def total(args):
    return sum(args)

print(total(90, 85, 95))  # 270
```

[Solution 10.9.1]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-9-1) &middot; [`ex_10_9_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_9_1.py)

### Exercise 10.9.2 — The star on args
{: #ex-10-9-2 }

This program should print all the extra numbers it receives as a tuple.

```python
def show_numbers(args):
    print(args)

show_numbers(1, 2, 3)  # (1, 2, 3)
```

[Solution 10.9.2]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-9-2) &middot; [`ex_10_9_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_9_2.py)

### Exercise 10.9.3 — Keyword collection
{: #ex-10-9-3 }

This program should print the keyword arguments as a dictionary.

```python
def show_options(*kwargs):
    print(kwargs)

show_options(color="blue", size="large")
# {'color': 'blue', 'size': 'large'}
```

[Solution 10.9.3]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-9-3) &middot; [`ex_10_9_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_9_3.py)

### Exercise 10.9.4 — Unpacking into a call
{: #ex-10-9-4 }

This program should pass the list as separate positional arguments and print 6.

```python
def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add_three(numbers))  # 6
```

[Solution 10.9.4]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-9-4) &middot; [`ex_10_9_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_9_4.py)

### Exercise 10.9.5 — Order of args and kwargs
{: #ex-10-9-5 }

This should print both the positional tuple and the keyword dictionary.

```python
def collect(**kwargs, *args):
    print(args)
    print(kwargs)

collect(1, 2, unit="cm")
```

[Solution 10.9.5]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-9-5) &middot; [`ex_10_9_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_9_5.py)

## Exercises 10.10.1–10.10.5

### Exercise 10.10.1 — Lambda syntax
{: #ex-10-10-1 }

This program should make a one-line function that squares a number and print 25.

```python
square = lambda x: return x * x

print(square(5))  # 25
```

[Solution 10.10.1]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-10-1) &middot; [`ex_10_10_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_10_1.py)

### Exercise 10.10.2 — Sorting with a key
{: #ex-10-10-2 }

This should sort the words from shortest to longest.

```python
words = ["pear", "fig", "banana"]
print(sorted(words, key=lambda w: -len(w)))
# ['fig', 'pear', 'banana']
```

[Solution 10.10.2]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-10-2) &middot; [`ex_10_10_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_10_2.py)

### Exercise 10.10.3 — Lambda with map
{: #ex-10-10-3 }

This should double every number in the list, giving `[2, 4, 6]`.

```python
numbers = [1, 2, 3]
doubled = list(map(lambda n: n + 2, numbers))
print(doubled)  # [2, 4, 6]
```

[Solution 10.10.3]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-10-3) &middot; [`ex_10_10_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_10_3.py)

### Exercise 10.10.4 — Lambda with filter
{: #ex-10-10-4 }

This should keep only the even numbers, giving `[2, 4]`.

```python
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda n: n % 2 == 1, numbers))
print(evens)  # [2, 4]
```

[Solution 10.10.4]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-10-4) &middot; [`ex_10_10_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_10_4.py)

### Exercise 10.10.5 — A lambda with two inputs
{: #ex-10-10-5 }

This should make a one-line function that adds two numbers and print 7.

```python
add = lambda a b: a + b

print(add(3, 4))  # 7
```

[Solution 10.10.5]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-10-5) &middot; [`ex_10_10_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_10_5.py)

## Exercises 10.11.1–10.11.5

### Exercise 10.11.1 — The shared default list
{: #ex-10-11-1 }

Each call should start with a fresh list, so both lines print a single-item list.

```python
def collect(item, basket=[]):
    basket.append(item)
    return basket

print(collect("apple"))   # ['apple']
print(collect("bread"))   # ['bread']
```

[Solution 10.11.1]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-11-1) &middot; [`ex_10_11_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_11_1.py)

### Exercise 10.11.2 — A safe default
{: #ex-10-11-2 }

This should add a reading to a fresh list each call, printing a one-item list each time.

```python
def add_reading(value, readings=[]):
    if readings is None:
        readings = []
    readings.append(value)
    return readings

print(add_reading(20))  # [20]
print(add_reading(22))  # [22]
```

[Solution 10.11.2]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-11-2) &middot; [`ex_10_11_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_11_2.py)

### Exercise 10.11.3 — Guarding the default
{: #ex-10-11-3 }

The guard should replace the shared default with a new list when none is given.

```python
def add_score(score, scores=None):
    if scores is None:
        scores = scores
    scores.append(score)
    return scores

print(add_score(90))  # [90]
```

[Solution 10.11.3]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-11-3) &middot; [`ex_10_11_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_11_3.py)

### Exercise 10.11.4 — Fresh dictionary each time
{: #ex-10-11-4 }

Each call should return a dictionary with just one entry.

```python
def tally(name, counts={}):
    counts[name] = 1
    return counts

print(tally("Maya"))   # {'Maya': 1}
print(tally("Luis"))   # {'Luis': 1}
```

[Solution 10.11.4]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-11-4) &middot; [`ex_10_11_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_11_4.py)

### Exercise 10.11.5 — Checking for None
{: #ex-10-11-5 }

The guard should run when no list is passed; both calls should print a one-item list.

```python
def append_day(day, days=None):
    if days == []:
        days = []
    days.append(day)
    return days

print(append_day("Mon"))  # ['Mon']
print(append_day("Tue"))  # ['Tue']
```

[Solution 10.11.5]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-11-5) &middot; [`ex_10_11_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_11_5.py)

## Exercises 10.12.1–10.12.5

### Exercise 10.12.1 — Mutating shares the change
{: #ex-10-12-1 }

Appending inside the function should change the caller's list too.

```python
def add_one(numbers):
    numbers = numbers + [1]

my_list = [10, 20]
add_one(my_list)
print(my_list)  # [10, 20, 1]
```

[Solution 10.12.1]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-12-1) &middot; [`ex_10_12_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_12_1.py)

### Exercise 10.12.2 — Rebinding stays local
{: #ex-10-12-2 }

Reassigning the parameter should not change the caller's list, so this prints the original.

```python
def replace(numbers):
    numbers.clear()
    numbers.extend([99, 100])

my_list = [10, 20]
replace(my_list)
print(my_list)  # [10, 20]
```

[Solution 10.12.2]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-12-2) &middot; [`ex_10_12_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_12_2.py)

### Exercise 10.12.3 — Integers are immutable
{: #ex-10-12-3 }

Changing the parameter inside the function should not affect the caller's number, which stays 5.

```python
def add_ten(value):
    global score
    score = value + 10

score = 5
add_ten(score)
print(score)   # expected: 5
```

[Solution 10.12.3]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-12-3) &middot; [`ex_10_12_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_12_3.py)

### Exercise 10.12.4 — Mutate in place
{: #ex-10-12-4 }

This should add a grade to the shared list in place, so the caller sees three items.

```python
def record_grade(grades, grade):
    grades = grades + [grade]

scores = [80, 90]
record_grade(scores, 100)
print(scores)  # [80, 90, 100]
```

[Solution 10.12.4]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-12-4) &middot; [`ex_10_12_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_12_4.py)

### Exercise 10.12.5 — Sharing the same object
{: #ex-10-12-5 }

Both names point to the same list, so the append should be visible outside; this prints a 4-item list.

```python
def append_value(items, value):
    items = list(items)
    items.append(value)

box = [1, 2, 3]
append_value(box, 4)
print(box)  # [1, 2, 3, 4]
```

[Solution 10.12.5]({{ site.baseurl }}/ep/solutions/10-functions/#sol-10-12-5) &middot; [`ex_10_12_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_10_12_5.py)

