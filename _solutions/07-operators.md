---
title: "Chapter 7: Operators — Solutions"
short_title: "Ch. 7 — Operators"
layout: post
permalink: /ep/solutions/07-operators/
order: 3
chapter: 7
---

Worked solutions to the 25 *Find the Bug* exercises in [Chapter 7: Operators]({{ site.baseurl }}/ep/exercises/07-operators/). Each one names the kind of bug, explains why the original misbehaved, and shows the corrected program.

Solutions stay folded until you open them — try the exercise first; the diagnosis is where the learning is.

## Solutions 7.1.1–7.1.5

### Solution 7.1.1 — Average of three test scores
{: #sol-7-1-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Because `/` has higher precedence than `+`, only `score3` is divided by 3, so the answer is wrong. Wrap the sum in parentheses so the division applies to the whole total.

```python
score1 = 78
score2 = 85
score3 = 89
average = (score1 + score2 + score3) / 3
print(average)   # 84.0
```

[Back to Exercise 7.1.1]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-1-1) &middot; [`sol_7_1_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_1_1.py)

</details>

### Solution 7.1.2 — Rectangle area
{: #sol-7-1-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Area is length times width, but the program adds them, giving 8 instead of 15. Use `*` instead of `+`.

```python
length = 5
width = 3
area = length * width
print(area)   # 15
```

[Back to Exercise 7.1.2]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-1-2) &middot; [`sol_7_1_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_1_2.py)

</details>

### Solution 7.1.3 — Eggs left over
{: #sol-7-1-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Floor division `//` gives the number of full cartons (2), not the leftover eggs. The remainder operator `%` gives what is left over.

```python
total_eggs = 17
carton_size = 6
leftover = total_eggs % carton_size
print(leftover)   # 5
```

[Back to Exercise 7.1.3]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-1-3) &middot; [`sol_7_1_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_1_3.py)

</details>

### Solution 7.1.4 — Kinetic energy
{: #sol-7-1-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The formula multiplies speed by 2 instead of squaring it, giving 6.0 rather than 9.0. Use the power operator `**` to square the speed.

```python
mass = 2
speed = 3
energy = 0.5 * mass * speed ** 2
print(energy)   # 9.0
```

[Back to Exercise 7.1.4]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-1-4) &middot; [`sol_7_1_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_1_4.py)

</details>

### Solution 7.1.5 — Total cost with tax
{: #sol-7-1-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The call to `print` is missing its closing parenthesis, so the program will not parse. Add the `)`.

```python
price = 20
tax_rate = 0.10
total = price + price * tax_rate
print(total)   # 22.0
```

[Back to Exercise 7.1.5]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-1-5) &middot; [`sol_7_1_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_1_5.py)

</details>

## Solutions 7.2.1–7.2.5

### Solution 7.2.1 — Saving up for a bike
{: #sol-7-2-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The second line uses plain assignment `=` and overwrites the starting $60 with $45, so the final total is wrong. It should be augmented assignment `+=` to add the deposit.

```python
savings = 60
savings += 45
savings += 45
print(savings)   # 150
```

[Back to Exercise 7.2.1]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-2-1) &middot; [`sol_7_2_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_2_1.py)

</details>

### Solution 7.2.2 — Counting down rocket seconds
{: #sol-7-2-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The line `seconds_left =- 3` is parsed as assigning the value `-3`, not as subtracting 3. The intended augmented-assignment operator is `-=`.

```python
seconds_left = 10
seconds_left -= 3
print(seconds_left)   # 7
```

[Back to Exercise 7.2.2]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-2-2) &middot; [`sol_7_2_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_2_2.py)

</details>

### Solution 7.2.3 — Doubling a recipe
{: #sol-7-2-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

The variable is `cups_flour`, but `print` refers to `Cups_flour` with a capital C, raising a `NameError`. Match the name exactly.

```python
cups_flour = 2
cups_flour *= 2
print(cups_flour)   # 4
```

[Back to Exercise 7.2.3]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-2-3) &middot; [`sol_7_2_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_2_3.py)

</details>

### Solution 7.2.4 — Splitting candy among friends
{: #sol-7-2-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`/=` performs true division and produces `3.0`, a float, instead of the whole number 3. Use floor-division assignment `//=` to keep an integer count of pieces per friend.

```python
candy = 12
friends = 4
candy //= friends
print(candy)   # 3
```

[Back to Exercise 7.2.4]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-2-4) &middot; [`sol_7_2_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_2_4.py)

</details>

### Solution 7.2.5 — Running total of steps
{: #sol-7-2-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The line computes `total_steps + today_steps` but throws the result away because it never assigns it back. Use `+=` so the running total is updated.

```python
total_steps = 6000
today_steps = 4000
total_steps += today_steps
print(total_steps)   # 10000
```

[Back to Exercise 7.2.5]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-2-5) &middot; [`sol_7_2_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_2_5.py)

</details>

## Solutions 7.3.1–7.3.5

### Solution 7.3.1 — Passing grade check
{: #sol-7-3-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

A score of exactly 60 should pass, but `>` excludes 60 and gives `False`. Use `>=` to include the boundary.

```python
score = 60
passing = score >= 60
print(passing)   # True
```

[Back to Exercise 7.3.1]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-3-1) &middot; [`sol_7_3_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_3_1.py)

</details>

### Solution 7.3.2 — Are two distances equal?
{: #sol-7-3-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Runtime

Inside a function call, `distance_a = distance_b` is read as a keyword argument, so `print` raises a `TypeError` about an invalid keyword argument. Comparison needs the equality operator `==`.

```python
distance_a = 100
distance_b = 100
print(distance_a == distance_b)   # True
```

[Back to Exercise 7.3.2]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-3-2) &middot; [`sol_7_3_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_3_2.py)

</details>

### Solution 7.3.3 — Temperature in safe range
{: #sol-7-3-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The chained comparison `0 < temp_c > 100` checks that the temperature is above both 0 and 100, which is wrong. It should be `0 < temp_c < 100` to test the range between them.

```python
temp_c = 25
in_range = 0 < temp_c < 100
print(in_range)   # True
```

[Back to Exercise 7.3.3]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-3-3) &middot; [`sol_7_3_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_3_3.py)

</details>

### Solution 7.3.4 — Different answers
{: #sol-7-3-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The "not equal" operator is written `!=`, not `= !`, so the expression will not parse. Use `!=`.

```python
correct_answer = 42
student_answer = 38
print(student_answer != correct_answer)   # True
```

[Back to Exercise 7.3.4]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-3-4) &middot; [`sol_7_3_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_3_4.py)

</details>

### Solution 7.3.5 — Within speed limit
{: #sol-7-3-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

A speed of exactly 65 is within the limit, but `<` excludes it and gives `False`. Use `<=` to include the limit itself.

```python
speed = 65
limit = 65
within_limit = speed <= limit
print(within_limit)   # True
```

[Back to Exercise 7.3.5]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-3-5) &middot; [`sol_7_3_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_3_5.py)

</details>

## Solutions 7.4.1–7.4.5

### Solution 7.4.1 — Eligible to vote
{: #sol-7-4-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Voting requires both conditions, but `or` returns `True` when only one holds, so a non-citizen adult is wrongly allowed. Use `and` so both age and citizenship must be satisfied.

```python
age = 20
is_citizen = False
can_vote = age >= 18 and is_citizen
print(can_vote)   # False
```

[Back to Exercise 7.4.1]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-4-1) &middot; [`sol_7_4_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_4_1.py)

</details>

### Solution 7.4.2 — Weekend or holiday
{: #sol-7-4-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Either condition should let you sleep in, but `and` requires both to be true, giving `False`. Use `or`.

```python
is_weekend = False
is_holiday = True
sleep_in = is_weekend or is_holiday
print(sleep_in)   # True
```

[Back to Exercise 7.4.2]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-4-2) &middot; [`sol_7_4_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_4_2.py)

</details>

### Solution 7.4.3 — Not raining
{: #sol-7-4-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

`not` is a prefix operator and must come before its value; writing `is_raining not` will not parse. Move `not` in front to get `not is_raining`.

```python
is_raining = False
stay_dry = not is_raining
print(stay_dry)   # True
```

[Back to Exercise 7.4.3]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-4-3) &middot; [`sol_7_4_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_4_3.py)

</details>

### Solution 7.4.4 — Safe to swim
{: #sol-7-4-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

A boolean expression assigned to a variable must not end with a colon; the trailing `:` makes the line invalid. Remove it.

```python
lifeguard_on_duty = True
water_is_calm = True
safe_to_swim = lifeguard_on_duty and water_is_calm
print(safe_to_swim)   # True
```

[Back to Exercise 7.4.4]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-4-4) &middot; [`sol_7_4_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_4_4.py)

</details>

### Solution 7.4.5 — Free shipping
{: #sol-7-4-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

Free shipping needs the order over $50 *or* the customer to be a member, but `and` requires both, so a $30 member order returns `False`. Use `or`. (Note short-circuiting: with `or`, once `is_member` is true the result is true regardless of the order total.)

```python
order_total = 30
is_member = True
free_shipping = order_total > 50 or is_member
print(free_shipping)   # True
```

[Back to Exercise 7.4.5]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-4-5) &middot; [`sol_7_4_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_4_5.py)

</details>

## Solutions 7.5.1–7.5.5

### Solution 7.5.1 — Vowel check
{: #sol-7-5-1 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

The code used `not in`, which would report `False` for a real vowel. To confirm membership, use the `in` operator.

```python
letter = "e"
vowels = "aeiou"
is_vowel = letter in vowels
print(is_vowel)   # True
```

[Back to Exercise 7.5.1]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-5-1) &middot; [`sol_7_5_1.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_5_1.py)

</details>

### Solution 7.5.2 — Odd number not in list
{: #sol-7-5-2 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Syntax

The membership operator is the two-word phrase `not in`, written in that order; `in not` will not parse. Use `not in` so a value absent from the list yields `True`.

```python
even_numbers = [2, 4, 6, 8]
number = 7
result = number not in even_numbers
print(result)   # True
```

[Back to Exercise 7.5.2]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-5-2) &middot; [`sol_7_5_2.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_5_2.py)

</details>

### Solution 7.5.3 — Missing value check
{: #sol-7-5-3 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`measurement is not None` is `False` when the value really is `None`, the opposite of what we want. Use the identity operator `is` to test that the value is exactly `None`.

```python
measurement = None
is_missing = measurement is None
print(is_missing)   # True
```

[Back to Exercise 7.5.3]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-5-3) &middot; [`sol_7_5_3.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_5_3.py)

</details>

### Solution 7.5.4 — First planet in the list
{: #sol-7-5-4 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

List indexing starts at 0, so `planets[1]` is the second planet, "Venus". Use index `0` to get the first.

```python
planets = ["Mercury", "Venus", "Earth"]
first_planet = planets[0]
print(first_planet)   # Mercury
```

[Back to Exercise 7.5.4]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-5-4) &middot; [`sol_7_5_4.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_5_4.py)

</details>

### Solution 7.5.5 — Day in the schedule
{: #sol-7-5-5 }

<details markdown="1">
<summary>Show the diagnosis and the fix</summary>

**Bug type:** Logical

`not in` returns `False` when the day is present, the reverse of what we want. Use the `in` operator to confirm membership.

```python
schedule = ["Monday", "Wednesday", "Friday"]
has_wednesday = "Wednesday" in schedule
print(has_wednesday)   # True
```

[Back to Exercise 7.5.5]({{ site.baseurl }}/ep/exercises/07-operators/#ex-7-5-5) &middot; [`sol_7_5_5.py`]({{ site.baseurl }}/ep/assets/code/solutions/sol_7_5_5.py)

</details>

