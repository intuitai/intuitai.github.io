---
title: Table of Contents
layout: post
permalink: /ep/book/table-of-contents/
order: 2
---

All 21 chapters and 130 sections, in seven parts. Page numbers are the printed
book's. Chapters marked **free** are included in the
[sample PDF]({{ site.baseurl }}/ep/book/sample/); chapters marked with an exercise
count link straight to that chapter's *Find the Bug* set on this site.

<div class="ep-toc" markdown="0">
{%- for part in site.data.toc %}
  {%- if part.title and part.title != "" %}
  <div class="ep-toc__part">Part {{ part.part }} &middot; {{ part.title }}</div>
  {%- endif %}
  {%- for ch in part.chapters %}
    {%- assign ex_page = nil -%}
    {%- for ex in site.exercises -%}
      {%- assign ex_chapter = ex.chapter | append: "" -%}
      {%- if ex_chapter == ch.number -%}{%- assign ex_page = ex -%}{%- endif -%}
    {%- endfor -%}
  <div class="ep-toc__chapter">
    <h4><span class="ep-toc__num">{{ ch.number }}</span>{{ ch.title }}
      {%- if ch.number == "1" or ch.number == "2" %}<span class="ep-tag ep-tag--free">free sample</span>{% endif %}
      {%- if ex_page %}<a class="ep-tag" href="{{ site.baseurl }}{{ ex_page.url }}">{{ ex_page.exercise_count }} exercises</a>{% endif %}
    </h4>
    {%- if ch.sections.size > 0 %}
    <ul class="ep-toc__sections">
      {%- for sec in ch.sections %}
      <li><span class="ep-toc__num">{{ sec.number }}</span>{{ sec.title | markdownify | remove: "<p>" | remove: "</p>" }}</li>
      {%- endfor %}
    </ul>
    {%- endif %}
  </div>
  {%- endfor %}
{%- endfor %}
</div>

<div class="ep-note" markdown="1">
The book also carries a preface, a list of figures, a list of tables, and a full
index. This listing is generated directly from the book's own typeset table of
contents, so it stays in step with the manuscript.
</div>
