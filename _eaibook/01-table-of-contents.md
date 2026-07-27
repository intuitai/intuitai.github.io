---
title: "Everyday AI: Table of Contents"
seo_title: "Everyday AI — Full Table of Contents"
description: >
  The complete contents of Everyday AI, Volume I: seven chapters, from why AI
  matters now and what a large language model actually is, through reading,
  writing, learning and problem-solving with it, to hallucinations, bias and
  responsible use.
layout: post
permalink: /eai/book/table-of-contents/
order: 1
---

All seven chapters and every section. Chapters marked **free sample** are
included in the [sample PDF]({{ site.baseurl }}/eai/book/sample/).

<div class="ep-toc" markdown="0">
{%- for part in site.data.eai.toc %}
  {%- comment -%}
  Everyday AI has no \part divisions, so generate_toc.py wraps its chapters in
  a single part with an empty title and this header is skipped. The guard is
  kept rather than removed: the data file is generated, and a later edition
  that does add parts would then render them without a change here.
  {%- endcomment -%}
  {%- if part.title and part.title != "" %}
  <div class="ep-toc__part">Part {{ part.part }} &middot; {{ part.title }}</div>
  {%- endif %}
  {%- for ch in part.chapters %}
  <div class="ep-toc__chapter">
    <h4><span class="ep-toc__num">{{ ch.number }}</span>{{ ch.title }}
      {%- if ch.number == "1" or ch.number == "2" %}<span class="ep-tag ep-tag--free">free sample</span>{% endif %}
    </h4>
    {%- if ch.sections.size > 0 %}
    <ul class="ep-toc__sections">
      {%- for sec in ch.sections %}
      <li><span class="ep-toc__num">{{ sec.number }}</span>{{ sec.title }}</li>
      {%- endfor %}
    </ul>
    {%- endif %}
  </div>
  {%- endfor %}
{%- endfor %}
</div>

<div class="ep-note" markdown="1">
This listing is generated directly from the book's own typeset table of
contents, so it stays in step with the manuscript. The book also carries a list
of figures and the index shown above. Front matter is absent for a mechanical
reason rather than an editorial one: it is numbered in roman numerals, and the
generator that reads the book's contents file keeps only entries with an arabic
page number.
</div>

## How the seven chapters fit together

The book is three movements, not seven separate essays.

**Chapters 1 and 2 are the grounding.** Why this is worth your time, and what
the machine actually is. Nothing is asked of you but attention. These are the
two chapters in the [free sample]({{ site.baseurl }}/eai/book/sample/).

**Chapters 3 through 6 are the skills.** Chapter 3 puts the tools in front of
you and introduces prompting as a craft. Chapters 4, 5 and 6 then apply it to
the three things most people actually want help with — reading and research,
writing, and learning and problem-solving — one chapter each. Each closes with
three worked examples of how people use this in practice, most of them citing
published reporting or research, and each carries a *When It Goes Wrong* sidebar
showing a genuine failure and the check that catches it.

**Chapter 7 is the counterweight.** Why hallucinations happen, where bias comes
from, what synthetic media does to "reading critically", what happens to the
text you paste in, and what changes when the model can act rather than only
answer. It closes with a practical checklist for staying in charge.
