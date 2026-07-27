---
title: Everyday AI
seo_title: "Everyday AI — A Practical Guide to AI for the Rest of Us"
description: >
  A short, plain-English guide to using AI well: what a language model actually
  is, how to get good answers out of Claude, ChatGPT and Gemini, and how to
  check the answers before you trust them. Chapters 1 and 2 free to download.
layout: post
permalink: /eai/
order: 0
# See the note in _book/00-home.md: Jekyll's excerpt is everything up to the
# first blank line, and the Liquid comment below spans several, which makes it
# warn about a "modified excerpt" on every build. Nothing renders excerpts.
excerpt_separator: ""
---

{%- comment -%}
layout: post, not home -- for the same two reasons _book/00-home.md gives. The
theme's home layout emits an empty rel="next" href on a site with no _posts and
an empty baseurl, which html-proofer rejects, and it does not give the page
prev/next arrows through the collection.

This page's title is the bare book name because it heads its group in the
sidebar. The other Everyday AI pages prefix theirs -- see the note on
ordered_collections in _config.yml.
{%- endcomment -%}

<div class="ep-hero" markdown="0">
  <div class="ep-hero__cover">
    <img src="{{ site.baseurl }}/eai/assets/img/cover.png"
         alt="Cover of Everyday AI, Volume I: Basics of Artificial Intelligence, by Dr. Nobel Khandaker">
  </div>
  <div class="ep-hero__body">
    <span class="ep-kicker">Volume I &middot; Basics of Artificial Intelligence</span>
    <p class="ep-tagline"><strong>You do not need to understand a neural network
    to use one well.</strong> You need to know what the machine is actually
    doing, how to ask it for what you want, and how to tell when it is confidently
    wrong. This book teaches those three things and stops.</p>
    <p>A practical guide to artificial intelligence for people with no technical
    background &mdash; seven chapters, written for a tenth-grade reader and up,
    by a lead engineer with a doctorate in computer science.</p>
    <div class="ep-actions">
      <a class="ep-btn ep-btn--primary" href="{{ site.baseurl }}/eai/assets/pdf/everyday-ai-sample-chapters-1-2.pdf" download="everyday-ai-chapters-1-2.pdf">Download chapters 1&ndash;2 free (PDF)</a>
      <a class="ep-btn ep-btn--ghost" href="{{ site.baseurl }}/eai/book/table-of-contents/">See the contents</a>
    </div>
  </div>
</div>

{%- comment -%}
Both counts are derived from the generated contents data rather than typed, so
regenerating after the manuscript grows a chapter updates them together. A
literal 7 beside a computed section count was a drift trap.

Chapters are counted only where `number` is non-empty: the data also carries the
unnumbered back-matter Index entry, which is a contents line but not a chapter.
{%- endcomment -%}
{%- assign eai_chapters = 0 -%}
{%- assign eai_sections = 0 -%}
{%- for part in site.data.eai.toc -%}
  {%- for ch in part.chapters -%}
    {%- if ch.number != blank -%}{%- assign eai_chapters = eai_chapters | plus: 1 -%}{%- endif -%}
    {%- assign eai_sections = eai_sections | plus: ch.sections.size -%}
  {%- endfor -%}
{%- endfor -%}
<ul class="ep-facts" markdown="0">
  <li><b>{{ eai_chapters }}</b><span>chapters, start to finish</span></li>
  <li><b>{{ eai_sections }}</b><span>sections</span></li>
  <li><b>2</b><span>chapters free to download</span></li>
  <li><b>None</b><span>prior experience assumed</span></li>
</ul>

## The problem this book solves

Most writing about artificial intelligence is either breathless or dismissive,
and almost none of it is useful on a Tuesday afternoon when you have a document
to read, a letter to write, or a problem you cannot get started on.

The breathless version tells you everything is about to change and leaves you
with nothing to do about it. The dismissive version tells you it is autocomplete
and leaves you unable to explain why autocomplete just rewrote a nineteenth-century
letter at five reading levels in the time it takes to finish a coffee.

*Everyday AI* takes a third position: the machine is genuinely useful, it is
genuinely limited, and both facts are learnable in an afternoon.

## What it actually teaches

Chapter 1 opens in a high school south of Columbus, Ohio, where a history teacher
named Maria Delgado takes a four-hundred-word complaint written by a coal miner in
1894 and, in the time it takes to finish a cup of coffee, has five versions of it
pitched at five reading levels and a glossary explaining what a "scab" was. She has
never written a line of code. What she has is a new kind of literacy, and it is
made of exactly two habits.

<div class="ep-note" markdown="1">
**Ask well.** The craft of describing what you want precisely enough to get it —
role, goal, context, constraints, examples, and the willingness to try again.
Introduced in Chapter 3 and practiced in every chapter after it.

**Check before you trust.** A tool that is right ninety percent of the time is
dangerous *because* it is so often right. Chapter 4 turns that into a rule, and
Chapters 4, 5 and 6 each carry a *When It Goes Wrong* sidebar that works through
one real failure and the quick check that catches it: the hallucinated citation,
fluent prose that is confidently wrong, and the confident arithmetic slip.
</div>

Around those two habits, the book covers what the technology actually is
(Chapter 2), the three tools you are most likely to touch and how they differ
(Chapter 3), and then three chapters of applied skill: reading and research,
writing, and learning and problem-solving. Chapter 7 is the one that keeps the
rest honest — why models hallucinate, where bias comes from, what happens to
what you type, and how to stay in charge of a machine that can now take actions
on your behalf.

## How it explains things

Most chapters open on a person in a particular moment — Maria and her Sunday, a
graduate student with forty-one papers open in forty-one tabs, a tenth grader
stuck on a chemistry problem at nine at night. Where one of those people is a
composite drawn from how people actually work, the book says so in a footnote
rather than letting you assume otherwise, which tells you something about how
the rest of it is written.

Every idea that has a shape gets drawn, too — in plain characters, so the
diagram works in a printed book, on a phone, and read aloud:

```text
  +-------------------------------------------------------+
  | ARTIFICIAL INTELLIGENCE                               |
  | machines doing things we'd call "smart"               |
  |                                                       |
  |   +-----------------------------------------------+   |
  |   | MACHINE LEARNING                              |   |
  |   | programs that learn patterns from examples,   |   |
  |   | instead of being told every rule              |   |
  |   |                                               |   |
  |   |   +---------------------------------------+   |   |
  |   |   | DEEP LEARNING                         |   |   |
  |   |   | learning with many-layered            |   |   |
  |   |   | "neural networks"                     |   |   |
  |   |   |                                       |   |   |
  |   |   |   +-------------------------------+   |   |   |
  |   |   |   | LARGE LANGUAGE MODELS         |   |   |   |
  |   |   |   | deep learning, aimed at text  |   |   |   |
  |   |   |   | (ChatGPT, Claude, Gemini)     |   |   |   |
  |   |   |   +-------------------------------+   |   |   |
  |   |   +---------------------------------------+   |   |
  |   +-----------------------------------------------+   |
  +-------------------------------------------------------+
```

That is Figure 2.1, and it is the whole vocabulary problem in one picture: the
four words everybody uses interchangeably are not rivals, they are nested.
Every large language model is a kind of deep learning, which is a kind of
machine learning, which is a kind of artificial intelligence. Once the words are
clear, the machine stops feeling like magic and starts feeling like something
you can use.

## Who it is for

- **Anyone who has opened a chat window and not known what to type.** The book
  assumes no technical background whatsoever — no programming, no mathematics
  beyond arithmetic.
- **People who use these tools already and suspect they are using them badly.**
  Most of the gap between a vague answer and a useful one is in how the question
  was asked, and that is a teachable skill.
- **Teachers, students, and anyone with a policy to navigate.** Chapter 6 draws
  the line between learning *with* a machine and letting it do your homework —
  and is candid that the bill for the second one comes due on test day. Chapter 7
  covers disclosure, copyright and consent, and what should never be pasted into
  a chatbot at all.

<div class="ep-note" markdown="1">
**Who it is *not* for.** If you want to build with these models — fine-tuning,
retrieval pipelines, agent frameworks, evaluation harnesses — this is the wrong
book. It is called *Basics of Artificial Intelligence* on purpose, and it names
tools by what they are good for rather than by their APIs.
</div>

## A note on shelf life

The book names real products — Claude, ChatGPT, Gemini, NotebookLM, Ollama — and
quotes a real subscription price, rather than hiding behind a vagueness that
would age just as badly and help less.

What it deliberately does *not* do is chase version numbers. Chapter 3 teaches
you to read the menu — what a context window is, what a "thinking" mode buys
you, when to hand the model a file instead of a question — so the chapter still
works after the menu changes. Product names and prices will date. The two habits
will not: asking well and checking before you trust will still be the whole game
when everything in these pages has been replaced by its successor.

## Start here

- **[Read chapters 1 and 2 free]({{ site.baseurl }}/eai/book/sample/)** — nineteen
  pages, typeset exactly as the book is.
- **[Browse the table of contents]({{ site.baseurl }}/eai/book/table-of-contents/)** —
  all seven chapters and every section.
- **[Errata]({{ site.baseurl }}/eai/book/errata/)** — confirmed corrections, and how
  to report one.
- **[About the author]({{ site.baseurl }}/ep/book/author/)**

<p style="margin-top:2.5em;color:#57606a;font-size:0.92em;">
<em>Everyday AI</em>, Volume I: Basics of Artificial Intelligence &mdash; First
Edition, forthcoming from Intramotev Press. The sample chapters are free to
read; the full text is &copy; Dr. Nobel Khandaker, all rights reserved.
</p>
