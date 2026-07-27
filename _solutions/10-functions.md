---
title: "Chapter 10: Functions — Solutions"
short_title: "Ch. 10 — Functions"
layout: post
permalink: /ep/solutions/10-functions/
order: 6
chapter: 10
---

Worked solutions to the 60 *Find the Bug* exercises in [Chapter 10: Functions]({{ site.baseurl }}/ep/exercises/10-functions/). Each one names the kind of bug, explains why the original misbehaved, and shows the corrected program.

Solutions stay folded until you open them — try the exercise first; the diagnosis is where the learning is.

## Solutions 10.1.1–10.1.5

### Solution 10.1.1 — Defining and calling
{: #sol-10-1-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Writing `welcome` only refers to the function object; it does not run it. You must add parentheses to call it, `welcome()`, so the body executes.

```python
def welcome():
    print("Welcome to the science club!")

welcome()
```

[Back to Exercise 10.1.1]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-1-1) &middot; [`sol_10_1_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_1_1.py)

</details>

### Solution 10.1.2 — The colon
{: #sol-10-1-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `def` header must end with a colon. Without it Python cannot tell where the body begins and raises a `SyntaxError`.

```python
def boiling_point():
    print("Water boils at 100 degrees Celsius.")

boiling_point()
```

[Back to Exercise 10.1.2]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-1-2) &middot; [`sol_10_1_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_1_2.py)

</details>

### Solution 10.1.3 — The function body
{: #sol-10-1-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The body must be indented under the `def` line. An unindented `print` makes Python expect an indented block and raises an `IndentationError`.

```python
def days_in_week():
    print("A week has 7 days.")

days_in_week()
```

[Back to Exercise 10.1.3]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-1-3) &middot; [`sol_10_1_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_1_3.py)

</details>

### Solution 10.1.4 — Indenting the body
{: #sol-10-1-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The two body lines must share the same indentation. The second `print` is indented two spaces instead of four, so Python raises an `IndentationError`.

```python
def study_plan():
    print("Read the chapter.")
    print("Solve five problems.")

study_plan()
```

[Back to Exercise 10.1.4]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-1-4) &middot; [`sol_10_1_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_1_4.py)

</details>

### Solution 10.1.5 — Remember to call
{: #sol-10-1-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Defining a function never runs it. You must call `freezing_point()` for anything to appear on screen.

```python
def freezing_point():
    print("Water freezes at 0 degrees Celsius.")

freezing_point()
```

[Back to Exercise 10.1.5]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-1-5) &middot; [`sol_10_1_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_1_5.py)

</details>

## Solutions 10.2.1–10.2.5

### Solution 10.2.1 — Passing an argument
{: #sol-10-2-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The function needs one argument but the call passes none, raising a `TypeError`. Supply the name in the call.

```python
def greet_student(name):
    print("Hello,", name)

greet_student("Maya")
```

[Back to Exercise 10.2.1]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-2-1) &middot; [`sol_10_2_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_2_1.py)

</details>

### Solution 10.2.2 — Parameter order
{: #sol-10-2-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The arguments are passed in the wrong order, so `name` becomes 15 and `age` becomes "Maya". Pass the name first, then the age.

```python
def describe(name, age):
    print(name, "is", age, "years old")

describe("Maya", 15)
```

[Back to Exercise 10.2.2]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-2-2) &middot; [`sol_10_2_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_2_2.py)

</details>

### Solution 10.2.3 — Too many arguments
{: #sol-10-2-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The function takes two parameters but the call passes three, raising a `TypeError`. Pass exactly width and height.

```python
def rectangle_area(width, height):
    return width * height

print(rectangle_area(4, 6))
```

[Back to Exercise 10.2.3]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-2-3) &middot; [`sol_10_2_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_2_3.py)

</details>

### Solution 10.2.4 — Using the parameter
{: #sol-10-2-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The call uses `number`, a name that exists only inside the function, so Python raises a `NameError`. Pass an actual value such as 5.

```python
def double(number):
    return number * 2

print(double(5))
```

[Back to Exercise 10.2.4]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-2-4) &middot; [`sol_10_2_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_2_4.py)

</details>

### Solution 10.2.5 — Two parameters
{: #sol-10-2-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The formula uses `width` twice, ignoring the second parameter. It should be `2 * width + 2 * height` to use both arguments.

```python
def perimeter(width, height):
    return 2 * width + 2 * height

print(perimeter(3, 5))  # 16
```

[Back to Exercise 10.2.5]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-2-5) &middot; [`sol_10_2_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_2_5.py)

</details>

## Solutions 10.3.1–10.3.5

### Solution 10.3.1 — Return, do not print
{: #sol-10-3-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function prints instead of returning, so `total` becomes `None`. Use `return` so the caller receives the value.

```python
def add(a, b):
    return a + b

total = add(5, 7)
print(total)  # 12
```

[Back to Exercise 10.3.1]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-3-1) &middot; [`sol_10_3_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_3_1.py)

</details>

### Solution 10.3.2 — Return the right value
{: #sol-10-3-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Division binds tighter than addition, so only `c` is divided by 3. Wrap the sum in parentheses before dividing.

```python
def average_of_three(a, b, c):
    return (a + b + c) / 3

print(average_of_three(80, 90, 100))  # 90.0
```

[Back to Exercise 10.3.2]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-3-2) &middot; [`sol_10_3_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_3_2.py)

</details>

### Solution 10.3.3 — Returning early
{: #sol-10-3-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

A bare `return` exits immediately and yields `None`; the formula on the next line never runs. Put the expression on the `return` line.

```python
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

print(c_to_f(100))  # 212.0
```

[Back to Exercise 10.3.3]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-3-3) &middot; [`sol_10_3_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_3_3.py)

</details>

### Solution 10.3.4 — Return what was asked
{: #sol-10-3-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The `else` branch returns `a` instead of `b`, so the larger value is never returned when `b` is bigger. Return `b` in the `else` branch.

```python
def larger(a, b):
    if a > b:
        return a
    else:
        return b

print(larger(4, 9))  # 9
```

[Back to Exercise 10.3.4]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-3-4) &middot; [`sol_10_3_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_3_4.py)

</details>

### Solution 10.3.5 — Use the returned value
{: #sol-10-3-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The returned value is discarded and `area` is never defined, so printing it raises a `NameError`. Store the result, then print it.

```python
def square(side):
    return side * side

area = square(6)
print(area)  # 36
```

[Back to Exercise 10.3.5]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-3-5) &middot; [`sol_10_3_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_3_5.py)

</details>

## Solutions 10.4.1–10.4.5

### Solution 10.4.1 — A default value
{: #sol-10-4-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`greet` without parentheses does not call the function. Add `()` so it runs with the default name.

```python
def greet(name="friend"):
    print("Hello,", name)

greet()
```

[Back to Exercise 10.4.1]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-4-1) &middot; [`sol_10_4_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_4_1.py)

</details>

### Solution 10.4.2 — Default tax rate
{: #sol-10-4-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The body multiplies by the literal 0.8 instead of the `rate` parameter, charging 80 percent. Use `rate` so the default 0.08 applies.

```python
def with_tax(price, rate=0.08):
    return price + price * rate

print(with_tax(50))  # 54.0
```

[Back to Exercise 10.4.2]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-4-2) &middot; [`sol_10_4_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_4_2.py)

</details>

### Solution 10.4.3 — Overriding the default
{: #sol-10-4-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The call meant to keep the default 100 steps but passed 200 as the override, giving `2 * 200 = 400`. To get 200 for two days, pass 100 as the per-day count (or omit it to use the default).

```python
def total_steps(days, per_day=100):
    return days * per_day

print(total_steps(2, 100))  # 200
```

[Back to Exercise 10.4.3]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-4-3) &middot; [`sol_10_4_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_4_3.py)

</details>

### Solution 10.4.4 — Order of defaults
{: #sol-10-4-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

A parameter with a default cannot come before one without a default, so `def area(height=1, width)` is a `SyntaxError`. Put the non-default parameter first.

```python
def area(width, height=1):
    return width * height

print(area(width=5))  # 5
```

[Back to Exercise 10.4.4]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-4-4) &middot; [`sol_10_4_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_4_4.py)

</details>

### Solution 10.4.5 — The default is optional
{: #sol-10-4-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The first parameter `value` has no default, so calling `increase()` with no arguments raises a `TypeError`. Pass a value, or give `value` a default.

```python
def increase(value=0, by=10):
    return value + by

print(increase())  # 10
```

[Back to Exercise 10.4.5]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-4-5) &middot; [`sol_10_4_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_4_5.py)

</details>

## Solutions 10.5.1–10.5.5

### Solution 10.5.1 — Calling by name
{: #sol-10-5-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`grade=7` is an unexpected keyword argument the function does not accept, raising a `TypeError`. Pass only `name` and `age`.

```python
def introduce(name, age):
    print(name, "is", age, "years old")

introduce(name="Lina", age=12)
```

[Back to Exercise 10.5.1]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-5-1) &middot; [`sol_10_5_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_5_1.py)

</details>

### Solution 10.5.2 — Order independence
{: #sol-10-5-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The keyword values are swapped: `time=100` and `distance=5` give 0.05, not 20.0. Match each keyword to the intended value.

```python
def speed(distance, time):
    return distance / time

print(speed(distance=100, time=5))  # 20.0
```

[Back to Exercise 10.5.2]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-5-2) &middot; [`sol_10_5_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_5_2.py)

</details>

### Solution 10.5.3 — Spelling the keyword
{: #sol-10-5-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The keyword `temp` does not match the parameter `temperature`, raising a `TypeError`. Use the exact parameter name.

```python
def report(city, temperature):
    print(city, "is at", temperature, "degrees")

report(city="Denver", temperature=30)
```

[Back to Exercise 10.5.3]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-5-3) &middot; [`sol_10_5_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_5_3.py)

</details>

### Solution 10.5.4 — Keyword after positional
{: #sol-10-5-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

A positional argument cannot follow a keyword argument, so `score_line(name="Sam", 95)` is a `SyntaxError`. Either make both keywords or both positional.

```python
def score_line(name, points):
    print(name, "scored", points)

score_line(name="Sam", points=95)
```

[Back to Exercise 10.5.4]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-5-4) &middot; [`sol_10_5_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_5_4.py)

</details>

### Solution 10.5.5 — Mixing names and positions
{: #sol-10-5-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`time=3` is an unexpected keyword the function does not accept, raising a `TypeError`. Pass only the three real parameters.

```python
def interest(principal, rate, years):
    return principal * rate * years

print(interest(1000, years=3, rate=0.02))  # 60.0
```

[Back to Exercise 10.5.5]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-5-5) &middot; [`sol_10_5_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_5_5.py)

</details>

## Solutions 10.6.1–10.6.5

### Solution 10.6.1 — Returning a pair
{: #sol-10-6-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The function returns a single value, so unpacking into two names raises a `ValueError`. Return both `min` and `max` as a pair.

```python
def min_max(a, b, c):
    return min(a, b, c), max(a, b, c)

low, high = min_max(31.0, 36.5, 33.0)
print(low, high)  # 31.0 36.5
```

[Back to Exercise 10.6.1]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-6-1) &middot; [`sol_10_6_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_6_1.py)

</details>

### Solution 10.6.2 — Unpacking the result
{: #sol-10-6-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The pair is stored in one name `quotient`, and `remainder` is never defined, so printing it raises a `NameError`. Unpack into two names.

```python
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(17, 5)
print(quotient, remainder)  # 3 2
```

[Back to Exercise 10.6.2]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-6-2) &middot; [`sol_10_6_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_6_2.py)

</details>

### Solution 10.6.3 — Matching the count
{: #sol-10-6-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The function returns three values but only two names receive them, raising a `ValueError`. Return just the two values you unpack.

```python
def person():
    return "Luis", 14

name, age = person()
print(name, age)  # Luis 14
```

[Back to Exercise 10.6.3]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-6-3) &middot; [`sol_10_6_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_6_3.py)

</details>

### Solution 10.6.4 — Order of the tuple
{: #sol-10-6-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The tuple is returned as `(3, 8)` but the caller expects width first, so width prints as 3. Return width then height: `return 8, 3`.

```python
def dimensions():
    return 8, 3

width, height = dimensions()
print("width", width, "height", height)
```

[Back to Exercise 10.6.4]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-6-4) &middot; [`sol_10_6_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_6_4.py)

</details>

### Solution 10.6.5 — Returning both values
{: #sol-10-6-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The first `return` exits the function, so it returns a single integer and tuple unpacking raises a `TypeError`. Return both values in one tuple.

```python
def sum_and_product(a, b):
    return a + b, a * b

total, product = sum_and_product(4, 5)
print(total, product)  # 9 20
```

[Back to Exercise 10.6.5]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-6-5) &middot; [`sol_10_6_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_6_5.py)

</details>

## Solutions 10.7.1–10.7.5

### Solution 10.7.1 — No return means None
{: #sol-10-7-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function explicitly returns "done", so `result` is not `None`. Remove the `return` so the function returns `None` implicitly.

```python
def announce():
    print("The meeting starts now.")

result = announce()
print(result)  # None
```

[Back to Exercise 10.7.1]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-7-1) &middot; [`sol_10_7_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_7_1.py)

</details>

### Solution 10.7.2 — Forgetting to return
{: #sol-10-7-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function computes `answer` but never returns it, so it returns `None` and prints `None`. Add a `return`.

```python
def double(number):
    answer = number * 2
    return answer

print(double(7))  # 14
```

[Back to Exercise 10.7.2]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-7-2) &middot; [`sol_10_7_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_7_2.py)

</details>

### Solution 10.7.3 — Printing is not returning
{: #sol-10-7-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The function prints but returns `None`, so `area` is `None` and `area * 2` raises a `TypeError`. Return the value instead of printing it.

```python
def circle_area(radius):
    return 3.14 * radius * radius

area = circle_area(5)
print(area * 2)  # uses the area twice
```

[Back to Exercise 10.7.3]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-7-3) &middot; [`sol_10_7_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_7_3.py)

</details>

### Solution 10.7.4 — None in arithmetic
{: #sol-10-7-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The function never returns `total`, so it returns `None`, and `None + 5` raises a `TypeError`. Return the value.

```python
def base_value():
    total = 10
    return total

print(base_value() + 5)  # 15
```

[Back to Exercise 10.7.4]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-7-4) &middot; [`sol_10_7_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_7_4.py)

</details>

### Solution 10.7.5 — Expecting a value
{: #sol-10-7-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The function assigns `chosen` but never returns it, so `number` is `None`. Return `chosen`.

```python
def lucky_number():
    chosen = 42
    return chosen

number = lucky_number()
print(number)  # 42
```

[Back to Exercise 10.7.5]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-7-5) &middot; [`sol_10_7_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_7_5.py)

</details>

## Solutions 10.8.1–10.8.5

### Solution 10.8.1 — Triple quotes
{: #sol-10-8-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The string opens with a single double-quote but closes with triple single-quotes, so the quotes do not match and Python raises a `SyntaxError`. Use matching triple quotes.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add(2, 3))  # 5
```

[Back to Exercise 10.8.1]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-8-1) &middot; [`sol_10_8_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_8_1.py)

</details>

### Solution 10.8.2 — Docstring placement
{: #sol-10-8-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

A string becomes the docstring only when it is the first statement in the body; here it sits after an assignment, so `__doc__` is `None`. Move the docstring to the top.

```python
def to_meters(feet):
    """Convert feet to meters."""
    result = feet * 0.3048
    return result

print(to_meters.__doc__)  # Convert feet to meters.
```

[Back to Exercise 10.8.2]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-8-2) &middot; [`sol_10_8_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_8_2.py)

</details>

### Solution 10.8.3 — Reading the docstring
{: #sol-10-8-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The attribute is `__doc__`, not `__docs__`, so accessing it raises an `AttributeError`. Use the correct name.

```python
def half(number):
    """Return half of a number."""
    return number / 2

print(half.__doc__)
```

[Back to Exercise 10.8.3]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-8-3) &middot; [`sol_10_8_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_8_3.py)

</details>

### Solution 10.8.4 — Closing the quotes
{: #sol-10-8-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The triple-quoted docstring is never closed, so Python reads the rest of the file as part of the string and raises a `SyntaxError`. Close the docstring.

```python
def square_perimeter(side):
    """Return the perimeter of a square."""
    return side * 4

print(square_perimeter(3))  # 12
```

[Back to Exercise 10.8.4]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-8-4) &middot; [`sol_10_8_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_8_4.py)

</details>

### Solution 10.8.5 — Docstring, then code
{: #sol-10-8-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The triple-quoted docstring is opened with `"""` but never closed, so Python reads the rest of the file as one unterminated string and reports a syntax error. Close the docstring on the same line.

```python
def kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

print(kelvin.__doc__)   # Convert Celsius to Kelvin.
```

[Back to Exercise 10.8.5]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-8-5) &middot; [`sol_10_8_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_8_5.py)

</details>

## Solutions 10.9.1–10.9.5

### Solution 10.9.1 — Collecting positionals
{: #sol-10-9-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Without a `*`, `args` is a single parameter, so passing three numbers raises a `TypeError`. Add the star to collect them into a tuple.

```python
def total(*args):
    return sum(args)

print(total(90, 85, 95))  # 270
```

[Back to Exercise 10.9.1]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-9-1) &middot; [`sol_10_9_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_9_1.py)

</details>

### Solution 10.9.2 — The star on args
{: #sol-10-9-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`args` without a star accepts only one argument, so passing three raises a `TypeError`. Use `*args` to gather them.

```python
def show_numbers(*args):
    print(args)

show_numbers(1, 2, 3)  # (1, 2, 3)
```

[Back to Exercise 10.9.2]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-9-2) &middot; [`sol_10_9_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_9_2.py)

</details>

### Solution 10.9.3 — Keyword collection
{: #sol-10-9-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

A single star collects positional arguments; keyword arguments need two stars. With one star, the keyword call raises a `TypeError`. Use `**kwargs`.

```python
def show_options(**kwargs):
    print(kwargs)

show_options(color="blue", size="large")
# {'color': 'blue', 'size': 'large'}
```

[Back to Exercise 10.9.3]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-9-3) &middot; [`sol_10_9_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_9_3.py)

</details>

### Solution 10.9.4 — Unpacking into a call
{: #sol-10-9-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Passing the list as one argument fills only `a`, leaving `b` and `c` missing, which raises a `TypeError`. Unpack with a star: `add_three(*numbers)`.

```python
def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add_three(*numbers))  # 6
```

[Back to Exercise 10.9.4]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-9-4) &middot; [`sol_10_9_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_9_4.py)

</details>

### Solution 10.9.5 — Order of args and kwargs
{: #sol-10-9-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

`**kwargs` must come after `*args` in the definition, so `def collect(**kwargs, *args)` is a `SyntaxError`. Put `*args` first.

```python
def collect(*args, **kwargs):
    print(args)
    print(kwargs)

collect(1, 2, unit="cm")
```

[Back to Exercise 10.9.5]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-9-5) &middot; [`sol_10_9_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_9_5.py)

</details>

## Solutions 10.10.1–10.10.5

### Solution 10.10.1 — Lambda syntax
{: #sol-10-10-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

A lambda body is a single expression and cannot contain `return`, so `lambda x: return x * x` is a `SyntaxError`. Drop the `return`.

```python
square = lambda x: x * x

print(square(5))  # 25
```

[Back to Exercise 10.10.1]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-10-1) &middot; [`sol_10_10_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_10_1.py)

</details>

### Solution 10.10.2 — Sorting with a key
{: #sol-10-10-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The key `-len(w)` sorts longest first; for shortest first the key should be `len(w)`.

```python
words = ["pear", "fig", "banana"]
print(sorted(words, key=lambda w: len(w)))
# ['fig', 'pear', 'banana']
```

[Back to Exercise 10.10.2]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-10-2) &middot; [`sol_10_10_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_10_2.py)

</details>

### Solution 10.10.3 — Lambda with map
{: #sol-10-10-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The lambda adds 2 instead of doubling, so `1` becomes 3, not 2. Multiply by 2 to double each number.

```python
numbers = [1, 2, 3]
doubled = list(map(lambda n: n * 2, numbers))
print(doubled)  # [2, 4, 6]
```

[Back to Exercise 10.10.3]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-10-3) &middot; [`sol_10_10_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_10_3.py)

</details>

### Solution 10.10.4 — Lambda with filter
{: #sol-10-10-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`n % 2 == 1` keeps odd numbers, not even ones. Test `n % 2 == 0` to keep the even numbers.

```python
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)  # [2, 4]
```

[Back to Exercise 10.10.4]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-10-4) &middot; [`sol_10_10_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_10_4.py)

</details>

### Solution 10.10.5 — A lambda with two inputs
{: #sol-10-10-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

Lambda parameters must be separated by a comma, so `lambda a b: a + b` is a `SyntaxError`. Write `lambda a, b: a + b`.

```python
add = lambda a, b: a + b

print(add(3, 4))  # 7
```

[Back to Exercise 10.10.5]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-10-5) &middot; [`sol_10_10_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_10_5.py)

</details>

## Solutions 10.11.1–10.11.5

### Solution 10.11.1 — The shared default list
{: #sol-10-11-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The default list is created once and shared across calls, so it keeps growing. Use `None` as the default and build a fresh list inside.

```python
def collect(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(collect("apple"))   # ['apple']
print(collect("bread"))   # ['bread']
```

[Back to Exercise 10.11.1]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-11-1) &middot; [`sol_10_11_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_11_1.py)

</details>

### Solution 10.11.2 — A safe default
{: #sol-10-11-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The guard checks for `None`, but the default is a shared list, not `None`, so the guard never runs and the list grows. Make the default `None`.

```python
def add_reading(value, readings=None):
    if readings is None:
        readings = []
    readings.append(value)
    return readings

print(add_reading(20))  # [20]
print(add_reading(22))  # [22]
```

[Back to Exercise 10.11.2]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-11-2) &middot; [`sol_10_11_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_11_2.py)

</details>

### Solution 10.11.3 — Guarding the default
{: #sol-10-11-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The guard assigns `scores = scores`, leaving it `None`, so `append` raises an `AttributeError`. Assign a new empty list instead.

```python
def add_score(score, scores=None):
    if scores is None:
        scores = []
    scores.append(score)
    return scores

print(add_score(90))  # [90]
```

[Back to Exercise 10.11.3]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-11-3) &middot; [`sol_10_11_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_11_3.py)

</details>

### Solution 10.11.4 — Fresh dictionary each time
{: #sol-10-11-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The default dictionary is created once and shared, so entries accumulate across calls. Use `None` and create a fresh dictionary inside.

```python
def tally(name, counts=None):
    if counts is None:
        counts = {}
    counts[name] = 1
    return counts

print(tally("Maya"))   # {'Maya': 1}
print(tally("Luis"))   # {'Luis': 1}
```

[Back to Exercise 10.11.4]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-11-4) &middot; [`sol_10_11_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_11_4.py)

</details>

### Solution 10.11.5 — Checking for None
{: #sol-10-11-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The default is `None`, but the guard checks `== []`, which is never true for `None`, so `days.append` raises an `AttributeError` on the first call. Check `is None`.

```python
def append_day(day, days=None):
    if days is None:
        days = []
    days.append(day)
    return days

print(append_day("Mon"))  # ['Mon']
print(append_day("Tue"))  # ['Tue']
```

[Back to Exercise 10.11.5]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-11-5) &middot; [`sol_10_11_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_11_5.py)

</details>

## Solutions 10.12.1–10.12.5

### Solution 10.12.1 — Mutating shares the change
{: #sol-10-12-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`numbers = numbers + [1]` builds a new list and rebinds the local name, leaving the caller's list unchanged. Use `append`, which mutates the shared list.

```python
def add_one(numbers):
    numbers.append(1)

my_list = [10, 20]
add_one(my_list)
print(my_list)  # [10, 20, 1]
```

[Back to Exercise 10.12.1]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-12-1) &middot; [`sol_10_12_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_12_1.py)

</details>

### Solution 10.12.2 — Rebinding stays local
{: #sol-10-12-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`clear` and `extend` mutate the shared list in place, so the caller sees `[99, 100]`, not the original. To leave the caller unchanged, rebind the local name instead.

```python
def replace(numbers):
    numbers = [99, 100]

my_list = [10, 20]
replace(my_list)
print(my_list)  # [10, 20]
```

[Back to Exercise 10.12.2]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-12-2) &middot; [`sol_10_12_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_12_2.py)

</details>

### Solution 10.12.3 — Integers are immutable
{: #sol-10-12-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The `global` line makes the function overwrite the caller's `score`, so it prints 15. An integer is passed by sharing: reassigning the local `value` never affects the caller. Drop the `global` line and work with the parameter.

```python
def add_ten(value):
    value = value + 10

score = 5
add_ten(score)
print(score)   # 5
```

[Back to Exercise 10.12.3]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-12-3) &middot; [`sol_10_12_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_12_3.py)

</details>

### Solution 10.12.4 — Mutate in place
{: #sol-10-12-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`grades = grades + [grade]` rebinds the local name to a new list, so the caller's list is unchanged. Use `append` to mutate the shared list in place.

```python
def record_grade(grades, grade):
    grades.append(grade)

scores = [80, 90]
record_grade(scores, 100)
print(scores)  # [80, 90, 100]
```

[Back to Exercise 10.12.4]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-12-4) &middot; [`sol_10_12_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_12_4.py)

</details>

### Solution 10.12.5 — Sharing the same object
{: #sol-10-12-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`items = list(items)` makes a separate copy, so the append affects only the copy and the caller's list is unchanged. Append directly to the passed-in list.

```python
def append_value(items, value):
    items.append(value)

box = [1, 2, 3]
append_value(box, 4)
print(box)  # [1, 2, 3, 4]
```

[Back to Exercise 10.12.5]({{ site.baseurl }}/ep/exercises/10-functions/#ex-10-12-5) &middot; [`sol_10_12_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_10_12_5.py)

</details>

