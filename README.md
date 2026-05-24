# game-hosting-guides.github.io

Source for [Game Hosting Guides](https://game-hosting-guides.github.io) — independent Minecraft and game server hosting reviews.

## Local development

```sh
bundle install
bundle exec jekyll serve
```

Site builds to `_site/`. Open http://localhost:4000.

## Structure

- `index.md` — comparison hub / best-of list
- `reviews/` — long-form provider reviews (Jekyll collection)
- `_layouts/` — page templates
- `_includes/review-schema.html` — Schema.org Review JSON-LD
- `assets/css/style.css` — styles
- `_config.yml` — Jekyll config (SEO plugins enabled)

## Adding a review

Create `reviews/<provider-slug>.md` with this front matter:

```yaml
---
title: "Provider Name Review (2026)"
description: "One-sentence meta description, 140–160 chars."
provider_name: "Provider Name"
provider_url: "https://provider.com"
rating: 8.5
date: 2026-05-24
last_updated: 2026-05-24
---
```

The review layout automatically renders the rating badge, related-reviews sidebar, and Schema.org Review JSON-LD.
