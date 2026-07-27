---
title: "Everyday AI: Errata"
seo_title: "Everyday AI — Errata and Corrections"
description: >
  Confirmed corrections to Everyday AI, listed newest first, with what the text
  says and what it should say — plus how to report an error in the free sample
  chapters before the book reaches print.
layout: post
permalink: /eai/book/errata/
order: 3
---

Corrections to *Everyday AI, Volume I: Basics of Artificial Intelligence*,
First Edition, by Dr. Nobel Khandaker.

A book about not trusting confident answers had better be willing to be
corrected. This page lists confirmed errors as they are found, so that a reader
who hits a passage that will not add up can check whether the problem is theirs
or the book's.

{% assign errata = site.data.eai.errata %}
{% if errata and errata.size > 0 %}

Currently listing **{{ errata.size }}** correction{% if errata.size != 1 %}s{% endif %}.

{% for item in errata %}
{%- comment -%}
`!= blank`, not a bare truthiness test on item.page. The schema in
_data/eai/errata.yml tells authors to write an empty string for a correction
that is not page-specific, and an empty string is TRUTHY in Liquid -- so a bare
test takes the "Page" branch and emits a heading reading "Page" with nothing
after it. The General branch would only ever fire if the key were omitted
entirely, which the documented schema never asks for.

Note the guard is described here rather than quoted: Liquid tokenises tags
inside comments, so writing one out literally is a syntax error, not
documentation. _book/00-home.md makes the same point.
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

Please report anything that looks wrong. The small ones matter as much as the
large ones, and because the book is still ahead of its first printing, a
correction sent now can be fixed before it reaches paper.

The most useful reports are on
**[GitHub Issues](https://github.com/nobelk/everyday-ai/issues)**, because the
thread stays visible to other readers who hit the same thing. If you would
rather not use GitHub, email works too.

When you report, please include:

- **Where.** The chapter and section number — "Section 2.3" is unambiguous — and
  the printed page number if you have one.
- **What it says.** A short quotation is ideal.
- **What you think it should say**, and briefly why.
- **Which format** you were reading: the
  [sample PDF]({{ site.baseurl }}/eai/book/sample/), a page on this site, or the
  book itself.

## What counts

<div class="ep-note" markdown="1">
Worth reporting:

- A factual claim that is wrong — a date, a figure, an attribution, a
  description of what a tool does.
- A **dead or wrong citation.** Chapter 1 alone carries several footnotes with
  live source links; a link that has rotted or that does not support the
  sentence it is attached to is an error worth fixing.
- A **stale product fact.** The book names real tools and quotes a real
  subscription price, current to mid-2026. When a price, a limit or a feature
  changes, that is a legitimate correction, and it is the kind this book will
  attract most.
- A definition that is technically wrong, or an analogy that misleads more than
  it explains.
- A cross-reference pointing at the wrong chapter, section or figure.
- Typos that change the meaning — a dropped "not" is worth more than a hundred
  transposed letters.

Probably not errata, though still worth raising:

- Style preferences, or a different way you would have explained something.
- Disagreement with a judgement call — which tool is better for which job, or
  how much to worry about a given risk. The book takes positions on purpose and
  says when it is doing so.
</div>

## A note on shelf life

Some of what this book says was true when it was written and will stop being
true — that is unavoidable in a book about a field moving this fast, and the
book flags its own time-sensitive claims rather than pretending otherwise.

Corrections of that kind are still welcome here. A reader in 2028 hitting a
2026 price is better served by a note on this page than by silence.

Reported errors are credited by name on this page unless you ask otherwise.
