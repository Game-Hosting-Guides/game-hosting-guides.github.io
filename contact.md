---
layout: default
title: "Contact Game Hosting Guides"
description: "Get in touch with the Game Hosting Guides team — provider corrections, feedback, and guest tips welcome."
permalink: /contact/
---

<section class="hero">
  <span class="eyebrow">Contact</span>
  <h1>Get in touch</h1>
  <p class="lede">Spotted an outdated price, a broken link, or a host we should review? Email us directly — we read every message.</p>
</section>

<section class="section" style="max-width: 680px;">
  <p style="font-size: 1.4rem; font-family: var(--serif); font-weight: 700;">
    <a href="mailto:{{ site.contact_email }}?subject=Game%20Hosting%20Guides%20%E2%80%94%20Contact">{{ site.contact_email }}</a>
  </p>
  <p class="meta">Or use the form below — it opens your email client with the message pre-filled.</p>

  <form action="mailto:{{ site.contact_email }}" method="GET" enctype="text/plain" class="contact-form">
    <label for="contact-subject">Subject</label>
    <input id="contact-subject" type="text" name="subject" placeholder="Provider correction · Guest tip · Feedback" required>

    <label for="contact-body">Message</label>
    <textarea id="contact-body" name="body" rows="6" placeholder="Tell us what's up." required></textarea>

    <button type="submit" class="btn btn--primary">Open email client</button>
  </form>

  <h2 style="border-top: 0; padding-top: 0; margin-top: 2.4em;">Other channels</h2>
  <p>If email isn't your thing, you can also reach us via:</p>
  <ul>
    <li><a href="{{ site.discord_url }}">Discord</a> &mdash; community discussion</li>
    <li><a href="{{ site.youtube_url }}" rel="noopener" target="_blank">YouTube</a> &mdash; comments on the latest video usually get a reply</li>
    <li><a href="{{ site.github_org_url }}" rel="noopener" target="_blank">GitHub</a> &mdash; if you'd like to read the site's open-source markdown directly</li>
  </ul>
</section>
