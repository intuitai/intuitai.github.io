---
title: "Chapter 18: Bugs — Solutions"
short_title: "Ch. 18 — Bugs"
layout: post
permalink: /ep/solutions/18-bugs/
order: 11
chapter: 18
---

Worked solutions to the 20 *Find the Bug* exercises in [Chapter 18: Bugs]({{ site.baseurl }}/ep/exercises/18-bugs/). Each one names the kind of bug, explains why the original misbehaved, and shows the corrected program.

Solutions stay folded until you open them — try the exercise first; the diagnosis is where the learning is.

## Solutions 18.1.1–18.1.5

### Solution 18.1.1 — Rectangle perimeter
{: #sol-18-1-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `def` header is missing the colon that must end every function definition line, so Python cannot parse the file. Adding the colon lets the function be defined and called.

```python
def perimeter(length, width):
    return 2 * (length + width)

print(perimeter(8, 5))   # 26
```

[Back to Exercise 18.1.1]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-1-1) &middot; [`sol_18_1_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_1_1.py)

</details>

### Solution 18.1.2 — Tip calculator
{: #sol-18-1-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The opening parenthesis after `bill *` is never closed, leaving an unbalanced bracket that the parser rejects. Closing the parenthesis fixes the expression.

```python
bill = 40.0
tip_rate = 0.15
total = bill + (bill * tip_rate)
print(total)   # 46.0
```

[Back to Exercise 18.1.2]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-1-2) &middot; [`sol_18_1_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_1_2.py)

</details>

### Solution 18.1.3 — Passing grade
{: #sol-18-1-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The condition uses `=` (assignment) where a comparison `==` is required, which is a syntax error inside an `if`. Using `>=` expresses the intended “score is at least 60” test.

```python
score = 72
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

[Back to Exercise 18.1.3]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-1-3) &middot; [`sol_18_1_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_1_3.py)

</details>

### Solution 18.1.4 — Weekly distance
{: #sol-18-1-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

There is a missing operator (or comma) between `tuesday` and `wednesday`; two names sitting side by side cannot be parsed. Adding the `+` sums all three days.

```python
monday = 3.2
tuesday = 4.1
wednesday = 2.7
total = monday + tuesday + wednesday
print(total)   # 10.0
```

[Back to Exercise 18.1.4]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-1-4) &middot; [`sol_18_1_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_1_4.py)

</details>

### Solution 18.1.5 — Counting change
{: #sol-18-1-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The `print` line is not indented under the `for`, so Python raises an `IndentationError` because a loop body is expected. Indenting the line by four spaces puts it inside the loop.

```python
coins = [25, 10, 5, 1]
for coin in coins:
    print(coin)
```

[Back to Exercise 18.1.5]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-1-5) &middot; [`sol_18_1_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_1_5.py)

</details>

## Solutions 18.2.1–18.2.5

### Solution 18.2.1 — Average speed
{: #sol-18-2-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Calling the function with `hours = 0` divides by zero at run time, raising `ZeroDivisionError`. Guarding against a zero time (or passing a real duration) avoids the crash.

```python
def average_speed(distance, hours):
    if hours == 0:
        return "Time cannot be zero"
    return distance / hours

print(average_speed(120, 2))   # 60.0
```

[Back to Exercise 18.2.1]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-2-1) &middot; [`sol_18_2_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_2_1.py)

</details>

### Solution 18.2.2 — Final price with tax
{: #sol-18-2-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The expression references `tax`, but the variable defined above is `tax_rate`, so Python raises a `NameError`. Using the correct name computes the taxed price.

```python
price = 50.0
tax_rate = 0.08
final_price = price + (price * tax_rate)
print(final_price)   # 54.0
```

[Back to Exercise 18.2.2]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-2-2) &middot; [`sol_18_2_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_2_2.py)

</details>

### Solution 18.2.3 — Doubling a recipe
{: #sol-18-2-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`cups_of_flour` is a string, and multiplying a string by a float raises `TypeError`. Storing the quantity as a number lets the multiplication work.

```python
cups_of_flour = 2.0
doubled = cups_of_flour * 2.0
print(doubled)   # 4.0
```

[Back to Exercise 18.2.3]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-2-3) &middot; [`sol_18_2_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_2_3.py)

</details>

### Solution 18.2.4 — Last student's score
{: #sol-18-2-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

`len(scores)` is 4, but valid indices run 0 to 3, so `scores[4]` raises `IndexError`. The last element is at index `len(scores) - 1` (or simply `-1`).

```python
scores = [88, 91, 79, 95]
last_index = len(scores) - 1
print(scores[last_index])   # 95
```

[Back to Exercise 18.2.4]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-2-4) &middot; [`sol_18_2_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_2_4.py)

</details>

### Solution 18.2.5 — Looking up a planet
{: #sol-18-2-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The key `"mars"` is lowercase, but the dictionary key is `"Mars"`; dictionary lookups are case sensitive, so this raises `KeyError`. Matching the stored key returns the value.

```python
moons = {"Earth": 1, "Mars": 2, "Venus": 0}
print(moons["Mars"])   # 2
```

[Back to Exercise 18.2.5]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-2-5) &middot; [`sol_18_2_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_2_5.py)

</details>

## Solutions 18.3.1–18.3.5

### Solution 18.3.1 — Rectangle area
{: #sol-18-3-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The program runs but uses `+` where area requires multiplication, so it returns 10 instead of 24. Multiplying length by width gives the correct area.

```python
def area(length, width):
    return length * width

print(area(6, 4))   # 24
```

[Back to Exercise 18.3.1]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-3-1) &middot; [`sol_18_3_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_3_1.py)

</details>

### Solution 18.3.2 — Average of three grades
{: #sol-18-3-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Operator precedence divides only `c` by 3 before adding, so the result is wrong. Parenthesizing the sum before dividing computes the true average.

```python
def average(a, b, c):
    return (a + b + c) / 3

print(average(80, 90, 100))   # 90.0
```

[Back to Exercise 18.3.2]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-3-2) &middot; [`sol_18_3_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_3_2.py)

</details>

### Solution 18.3.3 — Counting to ten
{: #sol-18-3-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`range(1, 10)` stops at 9 because the upper bound is excluded, so 10 is never printed (an off-by-one error). Using `range(1, 11)` includes 10.

```python
for number in range(1, 11):
    print(number)
```

[Back to Exercise 18.3.3]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-3-3) &middot; [`sol_18_3_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_3_3.py)

</details>

### Solution 18.3.4 — Discounted price
{: #sol-18-3-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Multiplying by the discount rate gives the amount taken off, not the price paid, so the result is 20 instead of 60. The customer pays the remaining fraction, `1 - discount_rate`.

```python
price = 80.0
discount_rate = 0.25
final_price = price * (1 - discount_rate)
print(final_price)   # 60.0
```

[Back to Exercise 18.3.4]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-3-4) &middot; [`sol_18_3_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_3_4.py)

</details>

### Solution 18.3.5 — Fahrenheit to Celsius
{: #sol-18-3-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The conversion factor is inverted: Fahrenheit to Celsius multiplies by `5 / 9`, not `9 / 5`. Swapping the fraction gives the right temperature.

```python
def f_to_c(f):
    return (f - 32) * 5 / 9

print(f_to_c(212))   # 100.0
```

[Back to Exercise 18.3.5]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-3-5) &middot; [`sol_18_3_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_3_5.py)

</details>

## Solutions 18.4.1–18.4.5

### Solution 18.4.1 — Total grocery cost
{: #sol-18-4-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Printing the subtotal reveals it is too low: the milk price is subtracted instead of added. Changing the `-` to `+` totals all three items.

```python
def total_cost(apples, bread, milk):
    subtotal = apples + bread + milk
    return subtotal

print(total_cost(3.50, 2.25, 1.75))   # 7.5
```

[Back to Exercise 18.4.1]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-4-1) &middot; [`sol_18_4_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_4_1.py)

</details>

### Solution 18.4.2 — Circle circumference
{: #sol-18-4-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Printing the returned value shows it is half the expected size: the formula omits the factor of 2 (circumference is `2 * pi * radius`). Adding the 2 corrects it.

```python
def circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

print(circumference(5))   # about 31.4
```

[Back to Exercise 18.4.2]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-4-2) &middot; [`sol_18_4_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_4_2.py)

</details>

### Solution 18.4.3 — Sum of a list
{: #sol-18-4-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Printing `total` inside the loop shows it only ever holds the latest value: the line replaces the running sum instead of adding to it. Using `+=` accumulates the total.

```python
rainfall = [1.2, 0.8, 2.0, 1.5]
total = 0
for amount in rainfall:
    total += amount
print(total)   # 5.5
```

[Back to Exercise 18.4.3]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-4-3) &middot; [`sol_18_4_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_4_3.py)

</details>

### Solution 18.4.4 — Sale price
{: #sol-18-4-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Printing `sale_price` shows it equals the discount amount, not the discounted price, so the subtraction yields the wrong savings. The savings are simply `price * discount_rate`.

```python
def savings(price, discount_rate):
    return price * discount_rate

print(savings(120, 0.30))   # 36.0
```

[Back to Exercise 18.4.4]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-4-4) &middot; [`sol_18_4_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_4_4.py)

</details>

### Solution 18.4.5 — Speed from distance and time
{: #sol-18-4-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Printing `result` reveals the division is inverted: speed is distance divided by time, not time divided by distance. Swapping the operands gives the correct speed.

```python
def speed(distance_km, time_hours):
    result = distance_km / time_hours
    return result

print(speed(150, 3))   # 50.0
```

[Back to Exercise 18.4.5]({{ site.baseurl }}/ep/exercises/18-bugs/#ex-18-4-5) &middot; [`sol_18_4_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_18_4_5.py)

</details>

