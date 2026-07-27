---
title: "Chapter 17: Testing"
short_title: "Ch. 17 — Testing"
layout: post
permalink: /ep/exercises/17-testing/
order: 10
chapter: 17
exercise_count: 15
---

15 *Find the Bug* exercises from Chapter 17 of *Everyday Programming*. Every program below is short, does something recognizable, and hides **exactly one** bug — syntax, runtime, or logical. Read it, predict what it does, then run it and find out.

Worked solutions for this chapter: [Chapter 17 solutions]({{ site.baseurl }}/ep/solutions/17-testing/). Every snippet is also available as a `.py` file — see [Exercises &amp; Solutions]({{ site.baseurl }}/ep/book/exercises/).

## Exercises 17.1.1–17.1.5

### Exercise 17.1.1 — Rectangle area check
{: #ex-17-1-1 }

The function should return the area of a rectangle, and the assert should pass for a 4 × 3 rectangle.

```python
def rectangle_area(length, width):
    return length + width

assert rectangle_area(4, 3) == 12
print("passed")
```

[Solution 17.1.1]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-1-1) &middot; [`ex_17_1_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_1_1.py)

### Exercise 17.1.2 — Celsius to Fahrenheit check
{: #ex-17-1-2 }

The function converts Celsius to Fahrenheit, and the assert should confirm that 100 °C is 212 °F.

```python
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

assert c_to_f(100) == 211
print("passed")
```

[Solution 17.1.2]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-1-2) &middot; [`ex_17_1_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_1_2.py)

### Exercise 17.1.3 — Average of three grades
{: #ex-17-1-3 }

The function should return the average of three test grades, and the assert should pass for grades 80, 90, and 100.

```python
def average(a, b, c):
    return a + b + c / 3

assert average(80, 90, 100) == 90
print("passed")
```

[Solution 17.1.3]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-1-3) &middot; [`ex_17_1_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_1_3.py)

### Exercise 17.1.4 — Percent of a total
{: #ex-17-1-4 }

The function should return what percent `part` is of `whole`, and the assert should pass for 25 out of 50.

```python
def percent(part, whole)
    return part / whole * 100

assert percent(25, 50) == 50
print("passed")
```

[Solution 17.1.4]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-1-4) &middot; [`ex_17_1_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_1_4.py)

### Exercise 17.1.5 — Total cost with tax
{: #ex-17-1-5 }

The function should add 10% tax to a price, and the assert should pass for a $20 item costing $22.

```python
def total_with_tax(price):
    return price + price * 0.10

assert total_with_tax(20) == 20
print("passed")
```

[Solution 17.1.5]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-1-5) &middot; [`ex_17_1_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_1_5.py)

## Exercises 17.2.1–17.2.5

### Exercise 17.2.1 — Perimeter test
{: #ex-17-2-1 }

This pytest function checks that the perimeter of a square with side 5 is 20.

```python
def square_perimeter(side):
    return 4 * side

def test_square_perimeter():
    assert square_perimeter(5) == 25
```

[Solution 17.2.1]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-2-1) &middot; [`ex_17_2_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_2_1.py)

### Exercise 17.2.2 — Speed test
{: #ex-17-2-2 }

This pytest function should verify that traveling 100 km in 2 hours gives a speed of 50 km/h.

```python
def speed(distance, time):
    return distance * time

def test_speed():
    assert speed(100, 2) == 50
```

[Solution 17.2.2]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-2-2) &middot; [`ex_17_2_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_2_2.py)

### Exercise 17.2.3 — Discount test
{: #ex-17-2-3 }

This pytest function should check that a 20% discount on a $50 item leaves a $40 price.

```python
def discounted_price(price, percent_off):
    return price - price * percent_off / 100

def test_discounted_price():
    assert discounted_price(50, 20) == 40
    return True
```

[Solution 17.2.3]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-2-3) &middot; [`ex_17_2_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_2_3.py)

### Exercise 17.2.4 — Counting even numbers
{: #ex-17-2-4 }

This pytest function should confirm that there are 3 even numbers in the list `[1, 2, 3, 4, 6]`.

```python
def count_evens(numbers):
    return len([n for n in numbers if n % 2 == 0])

def check_count_evens():
    assert count_evens([1, 2, 3, 4, 6]) == 3
```

[Solution 17.2.4]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-2-4) &middot; [`ex_17_2_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_2_4.py)

### Exercise 17.2.5 — Doubling a recipe
{: #ex-17-2-5 }

This pytest function should verify that doubling 3 cups of flour gives 6 cups.

```python
def double_recipe(cups):
    return cups * 2

def test_double_recipe():
    assert double_recipe(3) = 6
```

[Solution 17.2.5]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-2-5) &middot; [`ex_17_2_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_2_5.py)

## Exercises 17.3.1–17.3.5

### Exercise 17.3.1 — Sum of an empty list
{: #ex-17-3-1 }

This pytest function tests the edge case of summing an empty list, which should give 0.

```python
def total(numbers):
    running = 0
    for n in numbers:
        running += n
    return running

def test_total_empty():
    assert total([]) == 1
```

[Solution 17.3.1]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-3-1) &middot; [`ex_17_3_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_3_1.py)

### Exercise 17.3.2 — Floating-point area
{: #ex-17-3-2 }

This test checks the area of a circle of radius 2 (about 12.566) and should pass.

```python
import math

def area_circle(radius):
    return math.pi * radius ** 2

def test_area_circle():
    assert area_circle(2) == 12.566
```

[Solution 17.3.2]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-3-2) &middot; [`ex_17_3_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_3_2.py)

### Exercise 17.3.3 — Absolute value of negatives
{: #ex-17-3-3 }

This pytest function tests the edge case of a negative input, expecting `abs_value(-7)` to be 7.

```python
def abs_value(number):
    if number < 0:
        return number
    return number

def test_abs_value_negative():
    assert abs_value(-7) == 7
```

[Solution 17.3.3]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-3-3) &middot; [`ex_17_3_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_3_3.py)

### Exercise 17.3.4 — Parametrized squares
{: #ex-17-3-4 }

This parametrized pytest checks that squaring 0, 2, and 5 gives 0, 4, and 25.

```python
import pytest

def square(n):
    return n ** 2

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (2, 4),
    (5, 20),
])
def test_square(n, expected):
    assert square(n) == expected
```

[Solution 17.3.4]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-3-4) &middot; [`ex_17_3_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_3_4.py)

### Exercise 17.3.5 — Approximate division
{: #ex-17-3-5 }

This pytest function uses `pytest.approx` to check that dividing 1 by 3 is about 0.3333.

```python
import pytest

def divide(a, b):
    return a / b

def test_divide():
    assert divide(1, 3) == pytest.approx(0.3333, abs=0)
```

[Solution 17.3.5]({{ site.baseurl }}/ep/solutions/17-testing/#sol-17-3-5) &middot; [`ex_17_3_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_17_3_5.py)

