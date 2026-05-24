# How We Test and Score Minecraft Hosts

This page documents the criteria, weights, and rules behind every review on [gamehostingguides.com](https://gamehostingguides.com/reviews/). If a provider scores 9.0 in one of our reviews and 6.0 in another, this page explains why.

## The headline criterion: disclosed hardware

Above all other factors, **we weight hardware disclosure**. A provider that publishes its CPU model, RAM type, and storage class is signing up to deliver something specific. A provider that hides those details is keeping its options open — and in our experience, "options open" at budget pricing means whatever silicon was cheapest the day they racked the server.

This is why our two highest-rated providers — [ServerPrism](https://gamehostingguides.com/reviews/serverprism/) (9.0) and [CloudNord](https://gamehostingguides.com/reviews/cloudnord/) (8.7) — are smaller than BisectHosting or Apex but publish more about what you're actually paying for.

## The five dimensions

Every provider is scored on the same five dimensions:

### 1. Performance and hardware (35% weight)

- CPU model disclosure (yes/no, exact SKU vs family-only)
- CPU clock speed (single-thread is what matters for Minecraft)
- Dedicated vs shared cores
- RAM type (DDR4 vs DDR5, ECC vs non-ECC)
- Storage (NVMe vs SATA SSD, PCIe Gen3 vs Gen4)
- Network throughput claims (where disclosed)

### 2. Pricing (20% weight)

- Entry-tier monthly cost in USD (without multi-year contract discounts)
- Cost per GB of RAM at entry
- Cost progression (does the cost-per-GB drop at higher tiers, or stay flat?)
- Hidden fees (setup, IPv4 addresses, backups as paid add-ons)
- Refund window (we expect at least 72 hours for self-serve refunds)

### 3. Features (20% weight)

- Modpack one-click installer + library size
- Plugin manager
- Control panel quality (Multicraft vs Pterodactyl vs custom)
- Backup automation (count + retention)
- DDoS protection (layer 4 minimum, layer 7 a bonus)
- Sub-user / team support
- Scheduled tasks
- Console / file manager access

### 4. Locations (15% weight)

- Number of datacenter locations
- Geographic spread (US, EU, AU, SG, BR coverage)
- Whether the provider lets you choose
- Whether non-primary locations charge a surcharge

### 5. Support (10% weight)

- Channels (ticket / live chat / Discord)
- Hours (24/7 vs business hours)
- Response time claims and their credibility
- Third-party reputation (Trustpilot patterns, Reddit context — used as sanity check only, not primary signal)

## What we count as a "fact"

A fact is something the provider publishes on their own pricing page, plan comparison, or documentation. We do not treat the following as facts:

- Marketing claims without supporting detail ("blazing fast performance", "premium hardware", "industry-leading")
- Third-party review-site claims (we cross-check our own)
- Reddit anecdotes (used for sanity-check only, never as a rating input)
- Affiliate-incentivized review aggregations

If a provider doesn't publish a CPU model, we write **"not publicly disclosed"** rather than guess.

## What we count as an opinion

An opinion is anything that requires our judgment:

- The "rating" itself (numeric score)
- "Best for X" recommendations
- Whether we'd buy a plan ourselves
- Whether a tradeoff is acceptable at the price point

Opinions are clearly framed as opinions and supported by the disclosed facts.

## Score adjustments

Two things can move a score up or down outside the standard rubric:

**+1 adjustment** for:
- Unusual transparency about hardware (e.g. publishing CPU SKU at budget tier)
- Genuinely unique features that solve real problems (e.g. ServerPrism's split-plan billing across multiple servers)

**−1 adjustment** for:
- Aggressive contract lock-ins that obscure true monthly cost
- Marketing claims that contradict published specs
- Known reputation issues we can substantiate

## Affiliate disclosure

Some outbound links to hosting providers are affiliate links. We earn a commission if you sign up via those links at no additional cost to you. **Affiliate status never affects which providers we cover or the scores we give them.** Several providers in our comparisons have no affiliate relationship with us at all.

If you ever see a discrepancy between an affiliate-incentivized rating elsewhere and our rating, we'd rather lose the commission than the trust signal.

## Updating reviews

We aim to revisit each review at least quarterly. Big provider changes — major price moves, new datacenters, ownership changes (like Apex acquiring MCProHosting in 2024) — trigger immediate updates regardless of cadence.

## How to flag a mistake

Spot an error in any review? Use the [contact form](https://gamehostingguides.com/contact/) on the main site. We action factual corrections quickly and publish a "last updated" date on every review page so readers can see when each was last checked.

---

## See also

- [All provider reviews](https://gamehostingguides.com/reviews/)
- [Best Minecraft Server Hosting comparison](https://gamehostingguides.com/best-minecraft-server-hosting/)
- [Glossary of hosting terms](./Glossary)
