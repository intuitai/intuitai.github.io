---
title: "Chapter 13: Modules — Solutions"
short_title: "Ch. 13 — Modules"
layout: post
permalink: /ep/solutions/13-modules/
order: 8
chapter: 13
---

Worked solutions to the 10 *Find the Bug* exercises in [Chapter 13: Modules]({{ site.baseurl }}/ep/exercises/13-modules/). Each one names the kind of bug, explains why the original misbehaved, and shows the corrected program.

Solutions stay folded until you open them — try the exercise first; the diagnosis is where the learning is.

## Solutions 13.1.1–13.1.5

### Solution 13.1.1 — Square root with math
{: #sol-13-1-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The Pythagorean theorem adds the squares of the legs, but this code subtracts them, so `math.sqrt` receives 9-16=-7 and raises a `ValueError` (math domain error). Change the `-` to `+`.

```python
import math

leg_a = 3
leg_b = 4
hypotenuse = math.sqrt(leg_a ** 2 + leg_b ** 2)
print(hypotenuse)   # 5.0
```

[Back to Exercise 13.1.1]({{ site.baseurl }}/ep/exercises/13-modules/#ex-13-1-1) &middot; [`sol_13_1_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_13_1_1.py)

</details>

### Solution 13.1.2 — Circle area with pi
{: #sol-13-1-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`math.pi` is a value (a float), not a function, so calling it as `math.pi()` raises `TypeError: 'float' object is not callable`. Remove the parentheses and multiply by the value directly.

```python
import math

radius = 5
area = math.pi * radius ** 2
print(area)   # about 78.54
```

[Back to Exercise 13.1.2]({{ site.baseurl }}/ep/exercises/13-modules/#ex-13-1-2) &middot; [`sol_13_1_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_13_1_2.py)

</details>

### Solution 13.1.3 — Rolling a die
{: #sol-13-1-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`random.randint(a, b)` includes *both* endpoints, so `randint(1, 7)` can return 7, which is impossible on a six-sided die. Use `random.randint(1, 6)`.

```python
import random

roll = random.randint(1, 6)
print(roll)   # a number from 1 to 6
```

[Back to Exercise 13.1.3]({{ site.baseurl }}/ep/exercises/13-modules/#ex-13-1-3) &middot; [`sol_13_1_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_13_1_3.py)

</details>

### Solution 13.1.4 — Average test score
{: #sol-13-1-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The module was imported as `statistics`, but the call uses `statistic` (missing the final `s`), raising `NameError`. Use the same name in the call that you used in the import.

```python
import statistics

scores = [80, 90, 100, 70]
average = statistics.mean(scores)
print(statistics.mean(scores))   # 85
```

[Back to Exercise 13.1.4]({{ site.baseurl }}/ep/exercises/13-modules/#ex-13-1-4) &middot; [`sol_13_1_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_13_1_4.py)

</details>

### Solution 13.1.5 — Rounding a price up
{: #sol-13-1-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

With `from math import ceil`, the name brought into scope is `ceil`, not `math`, so `math.ceil(price)` raises `NameError`. Call `ceil(price)` directly.

```python
from math import ceil

price = 4.20
rounded_up = ceil(price)
print(rounded_up)   # 5
```

[Back to Exercise 13.1.5]({{ site.baseurl }}/ep/exercises/13-modules/#ex-13-1-5) &middot; [`sol_13_1_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_13_1_5.py)

</details>

## Solutions 13.2.1–13.2.5

### Solution 13.2.1 — Importing your own helper
{: #sol-13-2-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The import line asks for `c_to_k`, but `conversions.py` only defines `c_to_f`, so the import raises `ImportError`. Import the function that actually exists.

```python
# file: conversions.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

# file: main.py
from conversions import c_to_f

print(c_to_f(100))   # 212.0
```

[Back to Exercise 13.2.1]({{ site.baseurl }}/ep/exercises/13-modules/#ex-13-2-1) &middot; [`sol_13_2_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_13_2_1.py)

</details>

### Solution 13.2.2 — Calling with the module prefix
{: #sol-13-2-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

With `import geometry`, the function must be called through its module as `geometry.rectangle_area(...)`; the bare name `rectangle_area` is undefined and raises `NameError`. Add the module prefix.

```python
# file: geometry.py
def rectangle_area(width, height):
    return width * height

# file: main.py
import geometry

print(geometry.rectangle_area(4, 6))   # 24
```

[Back to Exercise 13.2.2]({{ site.baseurl }}/ep/exercises/13-modules/#ex-13-2-2) &middot; [`sol_13_2_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_13_2_2.py)

</details>

### Solution 13.2.3 — The main guard
{: #sol-13-2-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The guard uses a single `=` (assignment) instead of `==` (comparison), which is a syntax error inside an `if` condition. Use `==` to compare `__name__` with `"__main__"`.

```python
# file: conversions.py
def c_to_f(celsius):
    return celsius * 9 / 5 + 32

if __name__ == "__main__":
    print(c_to_f(100))   # 212.0
```

[Back to Exercise 13.2.3]({{ site.baseurl }}/ep/exercises/13-modules/#ex-13-2-3) &middot; [`sol_13_2_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_13_2_3.py)

</details>

### Solution 13.2.4 — Spelling the function name
{: #sol-13-2-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The call misspells the function as `square_permieter`; the module `shapes` has no such attribute, so it raises `AttributeError`. Spell it `square_perimeter` to match the definition.

```python
# file: shapes.py
def square_perimeter(side):
    return 4 * side

# file: main.py
import shapes

print(shapes.square_perimeter(5))   # 20
```

[Back to Exercise 13.2.4]({{ site.baseurl }}/ep/exercises/13-modules/#ex-13-2-4) &middot; [`sol_13_2_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_13_2_4.py)

</details>

### Solution 13.2.5 — Kelvin conversion formula
{: #sol-13-2-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The Celsius-to-Kelvin formula adds 273.15, but the function subtracts it, giving -273.15 instead of 273.15. Change the operator to `+`.

```python
# file: conversions.py
def c_to_k(celsius):
    return celsius + 273.15

# file: main.py
from conversions import c_to_k

print(c_to_k(0))   # 273.15
```

[Back to Exercise 13.2.5]({{ site.baseurl }}/ep/exercises/13-modules/#ex-13-2-5) &middot; [`sol_13_2_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_13_2_5.py)

</details>

