---
title: "CloudNord Review (2026): Disclosed Ryzen 7 at 4.9 GHz for EU Minecraft Hosting"
description: "CloudNord publishes exact CPU specs (Ryzen 7 7700, 4.9 GHz boost) at $3.99/mo. Our #2 budget Minecraft host for disclosed single-thread performance on EU nodes."
provider_name: "CloudNord"
provider_url: "https://cloudnord.net"
slug: cloudnord
rating: 8.7
date: 2026-05-24
last_updated: 2026-05-24
locations: ["London, UK", "Amsterdam, NL", "Nuremberg, DE", "New York, US", "Los Angeles, US", "Toronto, CA", "São Paulo, BR", "Mumbai, IN", "Singapore", "Sydney, AU"]
starting_price_usd: 3.99
starting_ram_gb: 2
cpu: "AMD Ryzen 7 7700 (4.9 GHz boost) or Intel Core i9-11900K, depending on node"
storage: "NVMe SSD, soft-uncapped"
ddos_protection: true
modpack_support: true
control_panel: "Pterodactyl (heavily customised)"
standout: "Publishes exact CPU model and clock (Ryzen 7 7700 at 4.9 GHz) at a $3.99/mo entry price — almost no competitor in this band names the silicon"
---

CloudNord is our **#2 rated Minecraft host** in both the [best cheap Minecraft server hosting](/guides/best-cheap-minecraft-server-hosting/) and [best Minecraft hosting for modpacks](/guides/best-minecraft-hosting-for-modpacks/) rankings, because they publish exactly which CPU you'll land on — an **AMD Ryzen 7 7700 boosting to 4.9 GHz**, or an **Intel Core i9-11900K** on certain nodes — at $3.99/mo for the 2 GB entry plan. That 4.9 GHz single-thread clock is the spec that actually matters for Minecraft, and almost no other host in this price band names the silicon at all.

Headquartered in London and registered as **Cloud Nord Limited** at Companies House (#13394754), CloudNord runs a deliberately compact footprint across three EU datacentres (London, Amsterdam, Nuremberg) with a global ring of secondary locations on a small surcharge. It does not try to out-cheap Shockbyte on raw price-per-GB or out-polish Apex on brand recognition. Instead it pitches transparent hardware, à la carte resource scaling, and a heavily customised Pterodactyl panel — a profile aimed squarely at admins who know what they're buying.

This review reflects pricing and policy details fetched on 24 May 2026. Where CloudNord's public pages were thin on specifics, we cross-referenced with third-party reviews and the provider's own knowledge base. Anything we could not verify is flagged.

## Why we rate it 8.7

Four specific reasons put CloudNord ahead of almost every other host at this price:

1. **Disclosed CPU model and clock at a $3.99/mo entry tier.** Mainstream hosts at this price say things like "high-clock CPUs" or "premium hardware." CloudNord says **Ryzen 7 7700, 4.9 GHz boost**. That difference — naming the silicon rather than gesturing at it — is the rating. You can look up Cinebench, Geekbench and real-world Minecraft TPS numbers for a Ryzen 7 7700 before you pay. You cannot do that with a "premium" mystery CPU.
2. **The disclosed CPU is genuinely the right CPU for Minecraft.** The Minecraft server main tick loop is, in practice, single-threaded. World generation, mob AI, redstone and most modded workloads are bottlenecked by how fast a single core can grind through one tick before the next one starts. A 4.9 GHz Zen 4 core is at or near the top of what the consumer silicon market produces for that workload. A budget host running an older Xeon or a low-clock EPYC core can have twice the core count and still hit lower TPS on a heavy modpack — because no core is fast enough.
3. **Full physical cores, not vCPU/thread allocation.** A "1 vCPU" plan on a typical budget competitor often means one hyperthread shared with other tenants. A CloudNord "1 core" allocation is a full physical core. Under sustained modded load, that distinction is the difference between a stable 20 TPS and a server that lag-spikes every time a mob farm ticks.
4. **À la carte scaling on EU-native infrastructure.** You scale RAM and CPU cores independently, in GBP-native pricing, on datacentres physically located in London / Amsterdam / Nuremberg — not US racks routed through Frankfurt. For European players this is real low-latency hosting, with hardware specs you can verify.

The honest framing: there are bigger, better-known hosts in this market. CloudNord is smaller than BisectHosting, Apex or Nodecraft. Its refund window is shorter than industry norms, it has no live chat, and if you land on the i9-11900K node rather than the Ryzen, you do not get the 4.9 GHz advantage. None of that changes the rating, because the rating is built on the specific axis where CloudNord wins: **disclosed hardware quality and single-thread clock at a budget price band**.

## Pricing and plans

CloudNord prices Minecraft hosting in GBP by default, with a currency switcher for EUR, USD and others. Java Edition base pricing starts at £3.10/mo (around $3.99 USD or €3.65 EUR at May 2026 rates), with a recurring 20% promotional discount frequently applied at signup. Crossplay (Geyser) hosting starts at roughly £3.32/mo.

The bigger story is the pricing structure itself: CloudNord is one of the few hosts that lets you scale RAM and CPU cores independently at checkout, instead of forcing you onto a fixed "Dirt/Gold/Diamond" ladder. Based on third-party testing, the à la carte rates land at roughly:

| Resource | Approximate cost |
|---|---|
| RAM | $1.00–$1.60 per GB/month |
| CPU core (full, not thread) | $1.00–$2.00 per core/month |
| Base / setup | Included in the entry plan |
| North America surcharge | ~$0.39–$1.00/mo on top |

Translating that into representative builds:

| Build | RAM | CPU | Approx. USD/mo | Suited for |
|---|---|---|---|---|
| Entry vanilla | 2 GB | 1 core | $3.99 | 3-5 player SMP, hobby box |
| Small plugin server | 4 GB | 1 core | ~$7.50 | 8-12 player Paper/Spigot |
| Modded sweet spot | 6 GB | 2 cores | ~$13.80 | All The Mods, Create-style packs |
| Heavy modpack | 10 GB | 3 cores | ~$22.00 | RLCraft, GTNH-lite, 15-25 players |
| Big community | 16 GB | 4 cores | ~$35.00 | Large modded SMP, networks |

A few things worth flagging:

- **Currency presentation**: GBP is the source currency, so EUR/USD figures shift with FX. The "starting at $3.99" headline can drift by ±$0.30 depending on the day.
- **Refund window**: a full refund is available within 3 days of purchase. That is shorter than Apex's 7 days and shorter than most of the industry; if you need long evaluation runways, this is the single biggest gap in the offer.
- **Payment**: PayPal, Stripe (cards), and cryptocurrency are accepted.
- **Storage**: described as "unlimited" with a soft cap; you can request increases via ticket.

The à la carte model is the real differentiator. If you want 8 GB of RAM but only need a single CPU core, you pay for exactly that, instead of buying a tier that bundles 4 cores you will never use. Compared to [BisectHosting](/reviews/bisecthosting/)'s Budget and Premium tiers, it is meaningfully cheaper for modded use cases in the 6-12 GB range, where competitors typically force a step up to a more expensive premium plan.

## Performance and hardware

This is where CloudNord earns its rating. Unlike most budget and mid-market Minecraft hosts, CloudNord publicly discloses its CPU lineup, and the silicon is genuinely strong:

- **AMD Ryzen 7 7700** — 8 cores, 16 threads, **4.9 GHz boost on shared nodes** (5.3 GHz peak on the chip). Zen 4 architecture, excellent single-thread performance, which is exactly what Minecraft's main tick loop needs.
- **Intel Core i9-11900K** — 8 cores, 16 threads, 5.3 GHz boost. Rocket Lake silicon, still fast on single-threaded workloads but several generations older than the Ryzen 7. If you specifically want the 4.9 GHz Zen 4 advantage, you want the Ryzen node.

Which CPU you get depends on the datacentre you select, and CloudNord does not let you cherry-pick the chip at checkout. According to their support, you can request a move post-signup if you specifically want the Ryzen 7 7700 (it's the preferred chip for heavily modded packs because of its stronger per-core performance under sustained load). This is a genuine caveat: if you land on the i9 node and the Ryzen is full, you have the older silicon until capacity opens up.

**Why the clock matters more than the core count for Minecraft.** The Minecraft server runs its world simulation on a single main thread. Every 50 ms (20 ticks per second), one core has to finish processing all entities, blocks, redstone, AI and chunk updates before the next tick starts. Miss that window and TPS drops. Adding more cores does not help past a small amount of background work (chunk I/O, network) — what helps is making the main core faster. A 4.9 GHz Zen 4 core is at the top end of what the consumer CPU market produces. A budget host running 2.4 GHz EPYC cores can have four times the thread count and still lose to CloudNord on a heavy modpack, because the bottleneck is single-thread, not parallel.

Storage is NVMe SSD across the fleet, DDR4 RAM, with 1 Gbps network on every node. The provider sells "full CPU cores" rather than the vCPU/thread allocation that most competitors use. That distinction matters: a "1 vCPU" plan on a competitor often means a single hyperthread shared with other tenants, while a CloudNord "1 core" allocation is a full physical core. In practice you get more consistent TPS under modded load.

The honest caveat is that we cannot independently benchmark every node. Smaller hosts can have wildly different experiences node-to-node, depending on how aggressively they pack tenants. CloudNord's third-party reviews and Trustpilot footprint (high overall rating across several hundred reviews as of May 2026) point to a host that does not oversell heavily, which matches the experience you would expect from a provider charging Ryzen 7 prices rather than rock-bottom prices.

## Datacenter locations

CloudNord's European footprint is the real reason most of its users pick it:

- **London, UK**
- **Amsterdam, Netherlands**
- **Nuremberg, Germany**

For a player base in the UK, Benelux, France, Germany, the Nordics or Iberia, those three locations cover most of Europe with sub-30 ms latency. Nuremberg in particular is one of the best-connected datacentre markets in continental Europe and is the location used by Hetzner, OVH and most of the serious German hosting community.

Outside the EU, CloudNord offers:

- **New York, Los Angeles** (US, +~$0.39-$1 surcharge)
- **Toronto** (Canada)
- **São Paulo** (Brazil)
- **Mumbai** (India)
- **Singapore**
- **Sydney** (Australia)

The North American surcharge is small and explicitly disclosed at checkout, but it's worth being honest: CloudNord is EU-first by design. Non-European players pay a surcharge they would not pay with a US-headquartered host, and the secondary nodes are smaller and less battle-tested than the EU primaries. If your player base is in North America, [BisectHosting](/reviews/bisecthosting/) or [Apex Hosting](/reviews/apex-hosting/) are the safer geographic fit even if their hardware disclosure is weaker.

For European players, the picture inverts. A lot of "European" Minecraft hosting offered by US-headquartered providers actually routes through one or two Tier-3 EU datacentres with mediocre peering. CloudNord being EU-incorporated and running its own EU presence gives it a real latency advantage for European players — something neither [Server.pro](/reviews/server-pro/) nor most US-first competitors can match.

## Features

The standard checklist is well covered:

- **Control panel**: a heavily modified Pterodactyl panel at game.cloudnord.net. More flexible than Multicraft, with live console, SFTP, scheduled tasks, MySQL databases, subuser management, and one-click modpack installs. Slightly steeper learning curve if you are coming from Multicraft on Apex or Shockbyte.
- **Modpack support**: one-click installation across CurseForge, Modrinth, FTB, Technic, ATLauncher and VoidsWrath, with custom JAR upload supported. This is one of the most comprehensive modpack launcher catalogues in the budget tier.
- **Backups**: automatic scheduled backups are included, with additional slots available as a paid add-on.
- **DDoS protection**: included on every plan; CloudNord does not break out the mitigation capacity in marketing material.
- **Free migrations**: assisted migration is available from other hosts on request.
- **Crossplay (Geyser/Floodgate)**: supported as a distinct product tier so Bedrock players can join Java servers.
- **Server versions**: Vanilla, Paper, Spigot, Purpur, Fabric, Forge, NeoForge and most major server JARs supported.
- **Subdomain**: free subdomain included; custom domains supported.

What is missing relative to larger competitors: there is no managed plugin marketplace, no proprietary "easy mode" GUI on top of Pterodactyl, and the knowledge base is smaller than Apex's or Bisect's. You are expected to be at least vaguely comfortable with Pterodactyl conventions.

## Support

Support is via ticket system and Discord, with a published knowledge base. There is **no live chat and no phone line** — if you need an instant human response at 2 AM, this is not the host for you. Languages: CloudNord advertises 25+ language options across its panel and storefront, though primary support is in English.

Third-party reviews consistently describe ticket response times in the range of "a few hours" to "under 24 hours", with Discord often faster for non-billing issues. This is broadly consistent with what you would expect from a smaller team — quicker turnaround on technical issues than a larger host, but no guarantee of around-the-clock first response.

Trustpilot sentiment as of May 2026 is strongly positive, with reviewers repeatedly highlighting personal attention from support staff and willingness to migrate or reconfigure on request. The flip side, also consistent with a smaller team, is that complex cases can occasionally bounce between ticket replies rather than getting resolved in a single touch.

## Pros and cons

### Pros

- **Discloses exact CPU model and clock** (Ryzen 7 7700 at 4.9 GHz boost, or i9-11900K) at a $3.99/mo entry — almost no competitor in this price band does this.
- **Single-thread performance prioritised**: Zen 4 at 4.9 GHz is at the top of what the consumer CPU market produces, and Minecraft's main tick loop is single-threaded.
- **Full-core CPU allocation** instead of vCPU/thread splits, with the option to scale cores independently of RAM.
- **EU-native infrastructure** in London, Amsterdam and Nuremberg — real low latency for European players, not US datacentres pretending to serve Europe. GBP-native pricing from a UK-registered company.
- **À la carte pricing** lets you buy exactly the RAM and CPU you need, which is unusual at this price point. Frequent 20% promo discounts.
- **Comprehensive modpack launcher support**: one-click installation across CurseForge, Modrinth, FTB, Technic, ATLauncher and VoidsWrath.
- **Pterodactyl panel** with live console, SFTP, scheduled tasks, MySQL and subuser management.
- **Personal support** that tends to respond within hours, with high Trustpilot scores.

### Cons

- **3-day refund window** is shorter than industry norm (Apex offers 7 days). The single biggest gap in the offer.
- **GBP-default pricing** means headline USD/EUR figures move with FX; not ideal if you want a predictable bill.
- **Pterodactyl learning curve** is steeper than Multicraft if you are migrating from Apex or Shockbyte.
- **Smaller than BisectHosting / Apex / Nodecraft** — smaller knowledge base, smaller support team, smaller global footprint.
- **EU-first** means non-European players pay a small surcharge and get higher latency on secondary nodes; if your players are in North America, a US-first host is a better geographic fit.
- **No node-level CPU selection at checkout** — you can request the Ryzen 7 chip post-signup, but not guarantee it during signup. If you land on the i9-11900K node, you have older silicon without the 4.9 GHz Zen 4 advantage.
- **No live chat or phone**; ticket and Discord only.
- **"Unlimited" storage is soft-capped** — increases require a support request.

## Who is CloudNord for?

CloudNord makes the most sense for:

- **European players** who are tired of paying for "EU" hosting that is actually a single rack in Frankfurt routed via New York. London, Amsterdam and Nuremberg cover Europe properly.
- **Performance-per-dollar seekers** running modded packs in the 6-12 GB RAM band, where the à la carte model and full-core CPU allocation produce noticeably better TPS than Multicraft-based budget hosts at similar prices.
- **Anyone who wants to know what CPU is running their server.** Most hosts at this price point will not tell you. CloudNord will, and the answer is a good one.
- **Pterodactyl-comfortable admins** who want SFTP, scheduled tasks and proper subuser management without paying enterprise prices.

It is probably not the right pick if you want the cheapest possible 1 GB hobby box (Shockbyte and similar budget shops will beat it), if you specifically need Multicraft, if you require 24/7 live chat with a large support organisation, or if your player base is primarily in North America. [ServerPrism](/reviews/serverprism/) is a closer EU-focused competitor if you want a similar profile from a different small operator, and [Apex Hosting](/reviews/apex-hosting/) remains the safer default if hand-holding matters more than hardware.

## Verdict

CloudNord earns **8.7/10** on the strength of a single, narrow but unusually important claim: at $3.99/mo they publish the exact CPU you'll run on, and that CPU is a 4.9 GHz Ryzen 7 7700 — the right chip for Minecraft's single-threaded main loop. Full-core allocation, à la carte scaling, EU-native infrastructure and comprehensive modpack launcher support reinforce the case. The trade-offs are real and disclosed: a 3-day refund window that's shorter than industry norm, no live chat, a smaller team than BisectHosting or Apex, and an i9-11900K secondary node that doesn't carry the Ryzen's clock advantage. For European admins who care about hardware quality at a budget price, it is one of the easiest small hosts to recommend with confidence — and our #2 pick in both the [cheap Minecraft hosting](/guides/best-cheap-minecraft-server-hosting/) and [modpack hosting](/guides/best-minecraft-hosting-for-modpacks/) guides.

## Frequently asked questions

### Is CloudNord based in Europe?

Yes. Cloud Nord Limited is a UK private limited company registered at Companies House (#13394754), headquartered in London. Its primary Minecraft datacentres are in London, Amsterdam and Nuremberg, with additional non-EU nodes on a small surcharge.

### How does CloudNord pricing compare to Apex Hosting?

CloudNord's entry plan is roughly $3.99/mo for 2 GB on Ryzen 7 / i9 hardware, versus Apex's $9.99/mo entry pricing for 1 GB. In the modded sweet spot (6 GB, 2 cores) CloudNord lands around $13-14/mo, which is significantly cheaper than Apex's equivalent tier while disclosing better CPU specs. Apex still has the edge on knowledge base size and managed-service polish; CloudNord wins on raw price-per-performance and EU latency.

### What CPU does CloudNord use?

AMD Ryzen 7 7700 (Zen 4, 8 cores, **4.9 GHz boost on shared nodes**, 5.3 GHz peak) or Intel Core i9-11900K (8 cores, up to 5.3 GHz boost), depending on the datacentre. Both are full physical cores rather than vCPU/thread splits. The Ryzen 7 7700 is the better pick for modded Minecraft because of its stronger sustained per-core performance and newer Zen 4 architecture — the spec that matters for Minecraft's single-threaded main tick loop.

### Does CloudNord support modpacks?

Yes. One-click installation is supported for CurseForge, Modrinth, Feed The Beast, Technic, ATLauncher and VoidsWrath. Custom JAR upload is supported for anything outside that catalogue, and the panel handles Forge, NeoForge and Fabric without manual setup.

### What is the refund policy?

A full refund is available within 3 days of purchase. That is shorter than Apex's 7-day window and shorter than most of the industry — it is the single biggest gap in CloudNord's offer for buyers who want a long evaluation runway.

### Is the control panel Multicraft?

No. CloudNord uses a heavily customised Pterodactyl panel. It is more powerful than Multicraft (live console, SFTP, scheduled tasks, MySQL, subusers) but has a steeper learning curve if you are migrating from a Multicraft-based host like Shockbyte or Apex.
