---
layout: default
title: "Game Hosting Guides on YouTube"
description: "Latest videos from the Game Hosting Guides YouTube channel — Minecraft hosting comparisons, performance tests, and server tips."
permalink: /videos/
---

<div class="hero">
  <h1>Videos</h1>
  <p class="lede">Latest uploads from <a href="https://www.youtube.com/@GameHostingGuides" rel="noopener" target="_blank">our YouTube channel</a>. Each one has a companion page below with the embed, key points, and links to relevant reviews.</p>
</div>

{% assign videos = site.videos | sort: "published" | reverse %}
{% if videos.size == 0 %}
<p><em>No videos yet — they'll appear here automatically when uploaded.</em></p>
{% else %}
<ul class="video-grid">
{% for v in videos %}
  <li>
    <a class="video-card{% if v.video_type == 'short' %} short{% endif %}" href="{{ v.url | relative_url }}">
      <span class="thumb{% if v.video_type == 'short' %} short{% endif %}" style="background-image:url('{{ v.thumbnail }}');"></span>
      <div class="body">
        <h3>{{ v.title | truncate: 80 }}</h3>
        <p class="meta">{{ v.published | date: "%b %-d, %Y" }}{% if v.video_type == 'short' %} · Short{% endif %}</p>
      </div>
    </a>
  </li>
{% endfor %}
</ul>
{% endif %}

<p><a href="{{ '/' | relative_url }}">&larr; Back to home</a></p>
