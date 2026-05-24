---
layout: default
title: "Minecraft Hosting Guides and Comparisons"
description: "Practical guides for picking, sizing, and getting the most out of Minecraft server hosting — buying advice, comparisons, and explainers."
permalink: /guides/
---

<section class="hero">
  <span class="eyebrow">Guides</span>
  <h1>Practical guides for Minecraft server hosting</h1>
  <p class="lede">Explainers, comparisons, and buying advice — written to actually help you decide, not to fill an SEO bingo card.</p>
</section>

{% assign guides = site.guides | sort: "date" | reverse %}
{% if guides.size == 0 %}
<p><em>No guides published yet.</em></p>
{% else %}
<ul class="review-grid">
{% for g in guides %}
  <li>
    <a class="review-card" href="{{ g.url | relative_url }}">
      {% if g.category %}<span class="card-rating" style="background:transparent; color:var(--accent-strong); padding:0;">{{ g.category }}</span>{% endif %}
      <div class="card-title">{{ g.title | replace: " (2026)", "" | replace: " (2026 Guide)", "" }}</div>
      <p class="card-desc">{{ g.description }}</p>
      <div class="card-meta">
        {% if g.reading_time %}<span><strong>{{ g.reading_time }}</strong> min read</span>{% endif %}
        {% if g.last_updated %}<span>Updated {{ g.last_updated }}</span>{% endif %}
      </div>
    </a>
  </li>
{% endfor %}
</ul>
{% endif %}

<p style="margin-top:2em;"><a href="{{ '/' | relative_url }}">&larr; Back to home</a></p>
