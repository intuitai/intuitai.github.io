---
title: Errata
seo_title: "Everyday Programming — Errata and Corrections"
description: >
  Confirmed corrections to the first edition of Everyday Programming, listed
  newest first, with the printed text, the correction, and the printing that
  carries the fix.
layout: post
permalink: /ep/book/errata/
order: 6
---

Corrections to *Everyday Programming, Volume I: Basics of Computer Programs*,
First Edition, published by Intramotev Press.

Every book of four hundred pages has mistakes in it, and a book with more than a
thousand code listings has more opportunities than most. Confirmed corrections are listed here
as they are found, so that a reader who hits a puzzling passage can check
whether the puzzle is theirs or the book's.

{% assign errata = site.data.errata %}
{% if errata and errata.size > 0 %}

Currently listing **{{ errata.size }}** correction{% if errata.size != 1 %}s{% endif %}.

{% for item in errata %}
{%- comment -%}
`!= blank`, not a bare truthiness test -- see the note in _eaibook/03-errata.md.
_data/errata.yml documents `page: ""` for a correction that is not
page-specific, and an empty string is truthy in Liquid, so a bare test would
emit a heading reading "Page" with nothing after it.
{%- endcomment -%}
### {% if item.page != blank %}Page {{ item.page }}{% else %}General{% endif %}{% if item.location %} — {{ item.location }}{% endif %}

**Printed:** {{ item.printed | markdownify | remove: "<p>" | remove: "</p>" }}

**Should read:** {{ item.corrected | markdownify | remove: "<p>" | remove: "</p>" }}
{% if item.note %}
{{ item.note }}
{% endif %}
{% if item.reported or item.fixed_in %}
<p style="font-size:0.86em;color:#57606a;">
{%- if item.reported %}Reported by {{ item.reported }}.{% endif %}
{%- if item.fixed_in %} Corrected in the {{ item.fixed_in | downcase }}.{% endif %}
</p>
{% endif %}
{% endfor %}

{% else %}

<div class="ep-empty" markdown="1">
**No errata reported yet for the First Edition.**

That is a statement about what has been reported, not a claim that the book is
perfect. If you have found something, the section below is how to tell us.
</div>

{% endif %}

## How to report an error

Please report anything that looks wrong — the small ones matter as much as the
large ones, and a typo that costs a beginner an hour is not a small one.

The most useful reports are on **[GitHub Issues](https://github.com/nobelk/everyday-programming/issues)**,
because the thread stays visible to other readers who hit the same thing. If you
would rather not use GitHub, email works too.

When you report, please include:

- **Where.** The printed page number, or the section or exercise number —
  `Exercise 9.4.2` is unambiguous and identical in print and on this site.
- **What it says.** A short quotation is ideal.
- **What you think it should say**, and briefly why.
- **Which format** you were reading: the printed book, the
  [sample PDF]({{ site.baseurl }}/ep/book/sample/), or a page on this site.

## What counts

<div class="ep-note" markdown="1">
Worth reporting:

- Code that does not run, or that runs and produces a different result from the
  one shown in the comment.
- A solution that misdiagnoses its bug, or fixes a different bug from the one in
  the exercise.
- A definition, formula, or claim that is factually wrong.
- A cross-reference pointing at the wrong chapter, section, figure, or exercise.
- Typos that change the meaning — `=` where `==` was meant, a dropped `not`, a
  wrong variable name in a listing.

Probably not errata, though still worth raising:

- Style preferences, or a different way you would have written a program.
- Anything about the exercise numbering: it is deliberately sparse, because the
  numbers follow the chapter and section that host each exercise rather than
  running consecutively.
</div>

## Errata in the exercises

The exercise and solution pages on this site are generated directly from the
book's source, so a correction to the book propagates here automatically on the
next build. If a program on this site disagrees with the same program in the
printed book, the printed book is the older of the two — please report it either
way, since a disagreement is itself a defect.

Reported errors are credited by name on this page unless you ask otherwise.
