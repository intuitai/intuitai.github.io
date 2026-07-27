---
title: "Chapter 17: Testing — Solutions"
short_title: "Ch. 17 — Testing"
layout: post
permalink: /ep/solutions/17-testing/
order: 10
chapter: 17
---

Worked solutions to the 15 *Find the Bug* exercises in [Chapter 17: Testing]({{ site.baseurl }}/ep/exercises/17-testing/). Each one names the kind of bug, explains why the original misbehaved, and shows the corrected program.

Solutions stay folded until you open them — try the exercise first; the diagnosis is where the learning is.

## Solutions 17.1.1–17.1.5

### Solution 17.1.1 — Rectangle area check
{: #sol-17-1-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function adds length and width instead of multiplying them, so it returns 7 and the assert fails. Area of a rectangle is length times width.

```python
def rectangle_area(length, width):
    return length * width

assert rectangle_area(4, 3) == 12
print("passed")
```

[Back to Exercise 17.1.1]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-1-1) &middot; [`sol_17_1_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_1_1.py)

</details>

### Solution 17.1.2 — Celsius to Fahrenheit check
{: #sol-17-1-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function is correct, but the expected value in the test is wrong: 100 °C is 212 °F, not 211. The fix corrects the expected value.

```python
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

assert c_to_f(100) == 212
print("passed")
```

[Back to Exercise 17.1.2]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-1-2) &middot; [`sol_17_1_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_1_2.py)

</details>

### Solution 17.1.3 — Average of three grades
{: #sol-17-1-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Operator precedence divides only `c` by 3 before adding, instead of dividing the whole sum. Parentheses around the sum fix the formula so the average is computed correctly.

```python
def average(a, b, c):
    return (a + b + c) / 3

assert average(80, 90, 100) == 90
print("passed")
```

[Back to Exercise 17.1.3]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-1-3) &middot; [`sol_17_1_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_1_3.py)

</details>

### Solution 17.1.4 — Percent of a total
{: #sol-17-1-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The function header is missing the colon at the end of the `def` line, so the file will not parse. Adding the colon fixes it.

```python
def percent(part, whole):
    return part / whole * 100

assert percent(25, 50) == 50
print("passed")
```

[Back to Exercise 17.1.4]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-1-4) &middot; [`sol_17_1_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_1_4.py)

</details>

### Solution 17.1.5 — Total cost with tax
{: #sol-17-1-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function is correct (20 + 2 = 22), but the expected value in the assert is 20 instead of 22, so the check fails. The fix corrects the expected value.

```python
def total_with_tax(price):
    return price + price * 0.10

assert total_with_tax(20) == 22
print("passed")
```

[Back to Exercise 17.1.5]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-1-5) &middot; [`sol_17_1_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_1_5.py)

</details>

## Solutions 17.2.1–17.2.5

### Solution 17.2.1 — Perimeter test
{: #sol-17-2-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function correctly returns 4 × 5 = 20, but the test asserts 25, so it fails. The fix corrects the expected value to 20.

```python
def square_perimeter(side):
    return 4 * side

def test_square_perimeter():
    assert square_perimeter(5) == 20
```

[Back to Exercise 17.2.1]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-2-1) &middot; [`sol_17_2_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_2_1.py)

</details>

### Solution 17.2.2 — Speed test
{: #sol-17-2-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Speed is distance divided by time, but the function multiplies them, returning 200 instead of 50. Changing `*` to `/` fixes the formula.

```python
def speed(distance, time):
    return distance / time

def test_speed():
    assert speed(100, 2) == 50
```

[Back to Exercise 17.2.2]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-2-2) &middot; [`sol_17_2_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_2_2.py)

</details>

### Solution 17.2.3 — Discount test
{: #sol-17-2-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

A pytest test should check with `assert` and not `return` a value; the trailing `return True` makes the test look like it passes regardless. Removing it leaves the assertion as the real check.

```python
def discounted_price(price, percent_off):
    return price - price * percent_off / 100

def test_discounted_price():
    assert discounted_price(50, 20) == 40
```

[Back to Exercise 17.2.3]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-2-3) &middot; [`sol_17_2_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_2_3.py)

</details>

### Solution 17.2.4 — Counting even numbers
{: #sol-17-2-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

pytest only discovers functions whose names start with `test_`; `check_count_evens` will never be collected or run. Renaming it to `test_count_evens` lets pytest find it.

```python
def count_evens(numbers):
    return len([n for n in numbers if n % 2 == 0])

def test_count_evens():
    assert count_evens([1, 2, 3, 4, 6]) == 3
```

[Back to Exercise 17.2.4]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-2-4) &middot; [`sol_17_2_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_2_4.py)

</details>

### Solution 17.2.5 — Doubling a recipe
{: #sol-17-2-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The assert uses a single `=` (assignment) instead of `==` (comparison), which is a syntax error. Using `==` fixes the comparison.

```python
def double_recipe(cups):
    return cups * 2

def test_double_recipe():
    assert double_recipe(3) == 6
```

[Back to Exercise 17.2.5]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-2-5) &middot; [`sol_17_2_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_2_5.py)

</details>

## Solutions 17.3.1–17.3.5

### Solution 17.3.1 — Sum of an empty list
{: #sol-17-3-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function correctly returns 0 for an empty list, but the test asserts 1, so the edge-case check fails. The fix corrects the expected value to 0.

```python
def total(numbers):
    running = 0
    for n in numbers:
        running += n
    return running

def test_total_empty():
    assert total([]) == 0
```

[Back to Exercise 17.3.1]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-3-1) &middot; [`sol_17_3_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_3_1.py)

</details>

### Solution 17.3.2 — Floating-point area
{: #sol-17-3-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Comparing a floating-point result with plain `==` fails here because `area_circle(2)` is 12.566370…, not exactly 12.566. Wrap the expected value in `pytest.approx` to allow a tiny tolerance.

```python
import math
import pytest

def area_circle(radius):
    return math.pi * radius ** 2

def test_area_circle():
    assert area_circle(2) == pytest.approx(12.566, abs=1e-3)
```

[Back to Exercise 17.3.2]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-3-2) &middot; [`sol_17_3_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_3_2.py)

</details>

### Solution 17.3.3 — Absolute value of negatives
{: #sol-17-3-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

For a negative input the function returns the number unchanged instead of negating it, so `abs_value(-7)` gives -7. Returning `-number` in the negative branch fixes the edge case.

```python
def abs_value(number):
    if number < 0:
        return -number
    return number

def test_abs_value_negative():
    assert abs_value(-7) == 7
```

[Back to Exercise 17.3.3]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-3-3) &middot; [`sol_17_3_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_3_3.py)

</details>

### Solution 17.3.4 — Parametrized squares
{: #sol-17-3-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The third parameter case expects 20, but 5² = 25, so that case fails. Correcting the expected value to 25 makes all parametrized cases pass.

```python
import pytest

def square(n):
    return n ** 2

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (2, 4),
    (5, 25),
])
def test_square(n, expected):
    assert square(n) == expected
```

[Back to Exercise 17.3.4]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-3-4) &middot; [`sol_17_3_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_3_4.py)

</details>

### Solution 17.3.5 — Approximate division
{: #sol-17-3-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Setting `abs=0` gives `pytest.approx` zero tolerance, so 0.3333… never matches 0.3333 and the test fails. Using a small tolerance (or the default) lets the approximate comparison succeed.

```python
import pytest

def divide(a, b):
    return a / b

def test_divide():
    assert divide(1, 3) == pytest.approx(0.3333, abs=1e-4)
```

[Back to Exercise 17.3.5]({{ site.baseurl }}/ep/exercises/17-testing/#ex-17-3-5) &middot; [`sol_17_3_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_17_3_5.py)

</details>

