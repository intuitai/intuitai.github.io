---
title: "Chapter 7: Operators"
short_title: "Ch. 7 — Operators"
layout: post
permalink: /ep/exercises/07-operators/
order: 3
chapter: 7
exercise_count: 25
---

25 *Find the Bug* exercises from Chapter 7 of *Everyday Programming*. Every program below is short, does something recognizable, and hides **exactly one** bug — syntax, runtime, or logical. Read it, predict what it does, then run it and find out.

Worked solutions for this chapter: [Chapter 7 solutions]({{ site.baseurl }}/ep/solutions/07-operators/). Every snippet is also available as a `.py` file — see [Exercises &amp; Solutions]({{ site.baseurl }}/ep/book/exercises/).

## Exercises 7.1.1–7.1.5

### Exercise 7.1.1 — Average of three test scores
{: #ex-7-1-1 }

This program should print the average of three test scores, which is `84.0`.

```python
score1 = 78
score2 = 85
score3 = 89
average = score1 + score2 + score3 / 3
print(average)   # expected: 84.0
```

[Solution 7.1.1]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-1-1) &middot; [`ex_7_1_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_1_1.py)

### Exercise 7.1.2 — Rectangle area
{: #ex-7-1-2 }

This program should compute the area of a rectangle (length times width) and print `15`.

```python
length = 5
width = 3
area = length + width
print(area)   # expected: 15
```

[Solution 7.1.2]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-1-2) &middot; [`ex_7_1_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_1_2.py)

### Exercise 7.1.3 — Eggs left over
{: #ex-7-1-3 }

A baker has 17 eggs and packs them into cartons of 6. This program should print how many eggs are left over after filling whole cartons, which is `5`.

```python
total_eggs = 17
carton_size = 6
leftover = total_eggs // carton_size
print(leftover)   # expected: 5
```

[Solution 7.1.3]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-1-3) &middot; [`ex_7_1_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_1_3.py)

### Exercise 7.1.4 — Kinetic energy
{: #ex-7-1-4 }

Kinetic energy is one-half times mass times speed squared. For a mass of 2 kg moving at 3 m/s this should print `9.0`.

```python
mass = 2
speed = 3
energy = 0.5 * mass * speed * 2
print(energy)   # expected: 9.0
```

[Solution 7.1.4]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-1-4) &middot; [`ex_7_1_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_1_4.py)

### Exercise 7.1.5 — Total cost with tax
{: #ex-7-1-5 }

An item costs $20 and tax is 10%. This program should print the total cost including tax, which is `22.0`.

```python
price = 20
tax_rate = 0.10
total = price + price * tax_rate
print(total   # expected: 22.0
```

[Solution 7.1.5]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-1-5) &middot; [`ex_7_1_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_1_5.py)

## Exercises 7.2.1–7.2.5

### Exercise 7.2.1 — Saving up for a bike
{: #ex-7-2-1 }

A bike costs $240 and you start with $60, then add $45 each of two weeks. This program should print your savings, which is `150`.

```python
savings = 60
savings = 45
savings += 45
print(savings)   # expected: 150
```

[Solution 7.2.1]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-2-1) &middot; [`ex_7_2_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_2_1.py)

### Exercise 7.2.2 — Counting down rocket seconds
{: #ex-7-2-2 }

This program should subtract 3 from a 10-second countdown and print the time remaining, which is `7`.

```python
seconds_left = 10
seconds_left =- 3
print(seconds_left)   # expected: 7
```

[Solution 7.2.2]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-2-2) &middot; [`ex_7_2_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_2_2.py)

### Exercise 7.2.3 — Doubling a recipe
{: #ex-7-2-3 }

A recipe needs 2 cups of flour, and this program should double it for a bigger batch, printing `4`.

```python
cups_flour = 2
cups_flour *= 2
print(Cups_flour)   # expected: 4
```

[Solution 7.2.3]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-2-3) &middot; [`ex_7_2_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_2_3.py)

### Exercise 7.2.4 — Splitting candy among friends
{: #ex-7-2-4 }

There are 12 pieces of candy to split evenly among 4 friends. This program should update the count to pieces-per-friend and print `3`.

```python
candy = 12
friends = 4
candy /= friends
print(candy)   # expected: 3
```

[Solution 7.2.4]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-2-4) &middot; [`ex_7_2_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_2_4.py)

### Exercise 7.2.5 — Running total of steps
{: #ex-7-2-5 }

This program should add today's 4{,}000 steps to yesterday's 6{,}000 and print the running total, which is `10000`.

```python
total_steps = 6000
today_steps = 4000
total_steps + today_steps
print(total_steps)   # expected: 10000
```

[Solution 7.2.5]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-2-5) &middot; [`ex_7_2_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_2_5.py)

## Exercises 7.3.1–7.3.5

### Exercise 7.3.1 — Passing grade check
{: #ex-7-3-1 }

A grade of 60 or above passes. For a score of 60 this program should print `True`.

```python
score = 60
passing = score > 60
print(passing)   # expected: True
```

[Solution 7.3.1]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-3-1) &middot; [`ex_7_3_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_3_1.py)

### Exercise 7.3.2 — Are two distances equal?
{: #ex-7-3-2 }

This program should check whether two measured distances are equal and print `True`.

```python
distance_a = 100
distance_b = 100
print(distance_a = distance_b)   # expected: True
```

[Solution 7.3.2]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-3-2) &middot; [`ex_7_3_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_3_2.py)

### Exercise 7.3.3 — Temperature in safe range
{: #ex-7-3-3 }

Water is liquid between 0 and 100 degrees Celsius. For 25 degrees this program should print `True`.

```python
temp_c = 25
in_range = 0 < temp_c > 100
print(in_range)   # expected: True
```

[Solution 7.3.3]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-3-3) &middot; [`ex_7_3_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_3_3.py)

### Exercise 7.3.4 — Different answers
{: #ex-7-3-4 }

This program should check whether a student's answer differs from the correct answer and print `True`.

```python
correct_answer = 42
student_answer = 38
print(student_answer = ! correct_answer)   # expected: True
```

[Solution 7.3.4]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-3-4) &middot; [`ex_7_3_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_3_4.py)

### Exercise 7.3.5 — Within speed limit
{: #ex-7-3-5 }

The speed limit is 65. For a speed of 65 this program should report that the driver is within the limit and print `True`.

```python
speed = 65
limit = 65
within_limit = speed < limit
print(within_limit)   # expected: True
```

[Solution 7.3.5]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-3-5) &middot; [`ex_7_3_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_3_5.py)

## Exercises 7.4.1–7.4.5

### Exercise 7.4.1 — Eligible to vote
{: #ex-7-4-1 }

A person may vote only if they are at least 18 *and* a citizen. This adult is not a citizen, so the program should print `False`.

```python
age = 20
is_citizen = False
can_vote = age >= 18 or is_citizen
print(can_vote)   # expected: False
```

[Solution 7.4.1]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-4-1) &middot; [`ex_7_4_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_4_1.py)

### Exercise 7.4.2 — Weekend or holiday
{: #ex-7-4-2 }

You can sleep in if it is a weekend or a holiday. This program should print `True`.

```python
is_weekend = False
is_holiday = True
sleep_in = is_weekend and is_holiday
print(sleep_in)   # expected: True
```

[Solution 7.4.2]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-4-2) &middot; [`ex_7_4_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_4_2.py)

### Exercise 7.4.3 — Not raining
{: #ex-7-4-3 }

This program should report that it is not raining and print `True`.

```python
is_raining = False
stay_dry = is_raining not
print(stay_dry)   # expected: True
```

[Solution 7.4.3]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-4-3) &middot; [`ex_7_4_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_4_3.py)

### Exercise 7.4.4 — Safe to swim
{: #ex-7-4-4 }

It is safe to swim if a lifeguard is on duty and the water is calm. This program should print `True`.

```python
lifeguard_on_duty = True
water_is_calm = True
safe_to_swim = lifeguard_on_duty and water_is_calm:
print(safe_to_swim)   # expected: True
```

[Solution 7.4.4]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-4-4) &middot; [`ex_7_4_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_4_4.py)

### Exercise 7.4.5 — Free shipping
{: #ex-7-4-5 }

Shipping is free if the order is over $50 or the customer is a member. This program should print `True` for a $30 order by a member.

```python
order_total = 30
is_member = True
free_shipping = order_total > 50 and is_member
print(free_shipping)   # expected: True
```

[Solution 7.4.5]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-4-5) &middot; [`ex_7_4_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_4_5.py)

## Exercises 7.5.1–7.5.5

### Exercise 7.5.1 — Vowel check
{: #ex-7-5-1 }

This program should report whether the letter is a vowel and print `True`.

```python
letter = "e"
vowels = "aeiou"
is_vowel = letter not in vowels
print(is_vowel)   # expected: True
```

[Solution 7.5.1]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-5-1) &middot; [`ex_7_5_1.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_5_1.py)

### Exercise 7.5.2 — Odd number not in list
{: #ex-7-5-2 }

This program should check that 7 is not among the listed even numbers and print `True`.

```python
even_numbers = [2, 4, 6, 8]
number = 7
result = number in not even_numbers
print(result)   # expected: True
```

[Solution 7.5.2]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-5-2) &middot; [`ex_7_5_2.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_5_2.py)

### Exercise 7.5.3 — Missing value check
{: #ex-7-5-3 }

This program should report that a measurement is missing (its value is `None`) and print `True`.

```python
measurement = None
is_missing = measurement is not None
print(is_missing)   # expected: True
```

[Solution 7.5.3]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-5-3) &middot; [`ex_7_5_3.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_5_3.py)

### Exercise 7.5.4 — First planet in the list
{: #ex-7-5-4 }

This program should print the first planet, `"Mercury"`.

```python
planets = ["Mercury", "Venus", "Earth"]
first_planet = planets[1]
print(first_planet)   # expected: Mercury
```

[Solution 7.5.4]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-5-4) &middot; [`ex_7_5_4.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_5_4.py)

### Exercise 7.5.5 — Day in the schedule
{: #ex-7-5-5 }

This program should report whether "Wednesday" is in the schedule and print `True`.

```python
schedule = ["Monday", "Wednesday", "Friday"]
has_wednesday = "Wednesday" not in schedule
print(has_wednesday)   # expected: True
```

[Solution 7.5.5]({{ site.baseurl }}/ep/solutions/07-operators/#sol-7-5-5) &middot; [`ex_7_5_5.py`]({{ site.baseurl }}/ep/assets/code/exercises/ex_7_5_5.py)

