---
title: "Chapter 18: Bugs"
short_title: "Ch. 18 — Bugs"
layout: post
permalink: /ep/exercises/18-bugs/
order: 11
chapter: 18
exercise_count: 20
---

20 *Find the Bug* exercises from Chapter 18 of *Everyday Programming*. Every program below is short, does something recognizable, and hides **exactly one** bug — syntax, runtime, or logical. Read it, predict what it does, then run it and find out.

Worked solutions for this chapter: [Chapter 18 solutions]({{ site.baseurl }}/ep/solutions/18-bugs/). Every snippet is also available as a `.py` file — see [Exercises &amp; Solutions]({{ site.baseurl }}/ep/book/exercises/).

## Exercises 18.1.1–18.1.5

### Exercise 18.1.1 — Rectangle perimeter
{: #ex-18-1-1 }

This program should print the perimeter of a rectangle that is 8 metres by 5 metres.

```python
def perimeter(length, width)
    return 2 * (length + width)

print(perimeter(8, 5))   # expected: 26
```

[Solution 18.1.1]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-1-1) &middot; [`ex_18_1_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_1_1.py)

### Exercise 18.1.2 — Tip calculator
{: #ex-18-1-2 }

This program should add a 15% tip to a $40 restaurant bill.

```python
bill = 40.0
tip_rate = 0.15
total = bill + (bill * tip_rate
print(total)   # expected: 46.0
```

[Solution 18.1.2]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-1-2) &middot; [`ex_18_1_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_1_2.py)

### Exercise 18.1.3 — Passing grade
{: #ex-18-1-3 }

This program should report whether a test score of 72 is a passing grade.

```python
score = 72
if score = 60:
    print("Pass")
else:
    print("Pass")
```

[Solution 18.1.3]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-1-3) &middot; [`ex_18_1_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_1_3.py)

### Exercise 18.1.4 — Weekly distance
{: #ex-18-1-4 }

This program should print the total distance walked over three days.

```python
monday = 3.2
tuesday = 4.1
wednesday = 2.7
total = monday + tuesday wednesday
print(total)   # expected: 10.0
```

[Solution 18.1.4]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-1-4) &middot; [`ex_18_1_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_1_4.py)

### Exercise 18.1.5 — Counting change
{: #ex-18-1-5 }

This program should print each coin value in a small pile of change.

```python
coins = [25, 10, 5, 1]
for coin in coins:
print(coin)
```

[Solution 18.1.5]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-1-5) &middot; [`ex_18_1_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_1_5.py)

## Exercises 18.2.1–18.2.5

### Exercise 18.2.1 — Average speed
{: #ex-18-2-1 }

This program should print average speed as distance divided by time.

```python
def average_speed(distance, hours):
    return distance / hours

print(average_speed(120, 0))
```

[Solution 18.2.1]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-2-1) &middot; [`ex_18_2_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_2_1.py)

### Exercise 18.2.2 — Final price with tax
{: #ex-18-2-2 }

This program should print a $50 item's price after 8% sales tax.

```python
price = 50.0
tax_rate = 0.08
final_price = price + (price * tax)
print(final_price)   # expected: 54.0
```

[Solution 18.2.2]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-2-2) &middot; [`ex_18_2_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_2_2.py)

### Exercise 18.2.3 — Doubling a recipe
{: #ex-18-2-3 }

This program should double the cups of flour in a recipe.

```python
cups_of_flour = "2"
doubled = cups_of_flour * 2.0
print(doubled)   # expected: 4.0
```

[Solution 18.2.3]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-2-3) &middot; [`ex_18_2_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_2_3.py)

### Exercise 18.2.4 — Last student's score
{: #ex-18-2-4 }

This program should print the score of the last student in the list.

```python
scores = [88, 91, 79, 95]
last_index = len(scores)
print(scores[last_index])   # expected: 95
```

[Solution 18.2.4]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-2-4) &middot; [`ex_18_2_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_2_4.py)

### Exercise 18.2.5 — Looking up a planet
{: #ex-18-2-5 }

This program should print the number of moons for Mars.

```python
moons = {"Earth": 1, "Mars": 2, "Venus": 0}
print(moons["mars"])   # expected: 2
```

[Solution 18.2.5]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-2-5) &middot; [`ex_18_2_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_2_5.py)

## Exercises 18.3.1–18.3.5

### Exercise 18.3.1 — Rectangle area
{: #ex-18-3-1 }

This program should print the area of a 6 by 4 rectangle.

```python
def area(length, width):
    return length + width

print(area(6, 4))   # expected: 24
```

[Solution 18.3.1]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-3-1) &middot; [`ex_18_3_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_3_1.py)

### Exercise 18.3.2 — Average of three grades
{: #ex-18-3-2 }

This program should print the average of three test grades.

```python
def average(a, b, c):
    return a + b + c / 3

print(average(80, 90, 100))   # expected: 90.0
```

[Solution 18.3.2]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-3-2) &middot; [`ex_18_3_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_3_2.py)

### Exercise 18.3.3 — Counting to ten
{: #ex-18-3-3 }

This program should print the numbers 1 through 10.

```python
for number in range(1, 10):
    print(number)
```

[Solution 18.3.3]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-3-3) &middot; [`ex_18_3_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_3_3.py)

### Exercise 18.3.4 — Discounted price
{: #ex-18-3-4 }

This program should print the price of a $80 jacket after a 25% discount.

```python
price = 80.0
discount_rate = 0.25
final_price = price * discount_rate
print(final_price)   # expected: 60.0
```

[Solution 18.3.4]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-3-4) &middot; [`ex_18_3_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_3_4.py)

### Exercise 18.3.5 — Fahrenheit to Celsius
{: #ex-18-3-5 }

This program should convert 212 degrees Fahrenheit to Celsius.

```python
def f_to_c(f):
    return (f - 32) * 9 / 5

print(f_to_c(212))   # expected: 100.0
```

[Solution 18.3.5]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-3-5) &middot; [`ex_18_3_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_3_5.py)

## Exercises 18.4.1–18.4.5

### Exercise 18.4.1 — Total grocery cost
{: #ex-18-4-1 }

This program should print the total cost of three grocery items, but the answer is wrong. Trace it with `print` and find the single wrong line.

```python
def total_cost(apples, bread, milk):
    subtotal = apples + bread - milk
    return subtotal

print(total_cost(3.50, 2.25, 1.75))   # expected: 7.5
```

[Solution 18.4.1]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-4-1) &middot; [`ex_18_4_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_4_1.py)

### Exercise 18.4.2 — Circle circumference
{: #ex-18-4-2 }

This program should print the circumference of a circle with radius 5, but the answer is wrong. Trace it with `print` and find the single wrong line.

```python
def circumference(radius):
    pi = 3.14159
    return pi * radius

print(circumference(5))   # expected: about 31.4
```

[Solution 18.4.2]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-4-2) &middot; [`ex_18_4_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_4_2.py)

### Exercise 18.4.3 — Sum of a list
{: #ex-18-4-3 }

This program should print the sum of the daily rainfall totals, but the answer is wrong. Trace it with `print` and find the single wrong line.

```python
rainfall = [1.2, 0.8, 2.0, 1.5]
total = 0
for amount in rainfall:
    total = amount
print(total)   # expected: 5.5
```

[Solution 18.4.3]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-4-3) &middot; [`ex_18_4_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_4_3.py)

### Exercise 18.4.4 — Sale price
{: #ex-18-4-4 }

This program should print the savings on a $120 item at 30% off, but the answer is wrong. Trace it with `print` and find the single wrong line.

```python
def savings(price, discount_rate):
    sale_price = price * discount_rate
    return price - sale_price

print(savings(120, 0.30))   # expected: 36.0
```

[Solution 18.4.4]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-4-4) &middot; [`ex_18_4_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_4_4.py)

### Exercise 18.4.5 — Speed from distance and time
{: #ex-18-4-5 }

This program should print speed in kilometres per hour, but the answer is wrong. Trace it with `print` and find the single wrong line.

```python
def speed(distance_km, time_hours):
    result = time_hours / distance_km
    return result

print(speed(150, 3))   # expected: 50.0
```

[Solution 18.4.5]({{ site.baseurl }}/ep/solutions/18-bugs/#sol-18-4-5) &middot; [`ex_18_4_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_18_4_5.py)

