---
layout: guide
title: "Why Is My Minecraft Server Lagging? How to Diagnose and Fix Low TPS (2026)"
description: "A practical 2026 guide to diagnosing Minecraft server lag — how to tell TPS lag from network lag, what actually causes each, and which fixes are worth paying for."
category: "Educational"
slug: why-is-my-minecraft-server-lagging
date: 2026-07-08
last_updated: 2026-07-08
reading_time: 9
related_reviews: [shockbyte, server-pro, bisecthosting, apex-hosting]
faq:
  - question: "How do I tell if my server lag is my host's fault or my internet's fault?"
    answer: "Run /tps (Paper) or install Spark. If TPS is a solid 20.0 but the game still feels laggy, the problem is network latency — your connection, the server's route, or datacenter distance — not the host's hardware. If TPS is sitting at 12-18, the server can't keep up with its own workload, which is a hardware, plugin, or configuration problem. The two failure modes have completely different fixes, and confusing them is the most common troubleshooting mistake."
  - question: "Will more RAM fix my server lag?"
    answer: "Usually not. Low TPS is almost always a CPU or configuration problem, not a memory one. More RAM only helps if your server is actively running out of memory and garbage-collection pauses are freezing the game — you can confirm this in Spark or your panel's resource graph. If RAM sits at 40-60% and TPS is still bad, adding RAM changes nothing. Minecraft's main tick loop is single-threaded, so CPU clock speed is what determines whether the server keeps up."
  - question: "What is a good TPS for a Minecraft server?"
    answer: "20.0 TPS is perfect — that's the target tick rate and it cannot go higher. Anything at or above 19.5 sustained feels smooth. Between 18 and 19.5 you'll notice occasional stutter under load. Below 15 the game feels visibly slow: mobs stutter, redstone misfires, and hits don't register. A healthy server holds 20.0 with brief dips during chunk generation or big explosions, then recovers immediately."
  - question: "Can changing view-distance really reduce lag?"
    answer: "Yes, and it's the single highest-impact free fix. Dropping server view-distance from the default 10 to 6 or 7 can cut tick time dramatically on a busy server, because the server stops loading, ticking, and sending chunks players can't meaningfully see anyway. Pair it with a lower simulation-distance (4-6) to stop entity and redstone processing in far chunks. Most players never notice the difference."
---

The first thing to know is that "lag" describes two completely different problems that happen to feel similar in-game, and they have opposite fixes. **Server-side lag** is low TPS — the server can't finish its work in time and the whole world slows down for everyone. **Network lag** is high latency — the server is running fine, but the data takes too long to reach you. Buying more RAM to fix network lag, or switching datacenters to fix a plugin that's tanking your TPS, is how people waste money and stay frustrated. This guide shows you how to tell them apart in under a minute, then what actually fixes each one.

## The 60-second diagnosis

Before changing anything, find out which problem you have. Type `/tps` on any Paper, Purpur, or Pufferfish server, or install [Spark](https://spark.lucko.me/) (the standard profiler, works on nearly every server type) and run `/spark tps`.

| What you see | What it means | Where to look next |
|---|---|---|
| TPS **20.0**, game still stutters for you | Network lag — the server is healthy | Your connection, route, and datacenter distance |
| TPS **20.0** for you, laggy for others | Network lag on their end, not the server | Their connection, or a regional routing issue |
| TPS **15-19**, laggy for everyone | Mild server-side lag | Plugins, view-distance, entity counts |
| TPS **below 15**, laggy for everyone | Serious server-side lag | CPU, garbage collection, a runaway plugin or farm |
| TPS fine, then drops **only during specific events** | Event-triggered lag | Chunk generation, big explosions, mob farms, world border fill |

TPS (ticks per second) is the server's heartbeat. It runs at a fixed target of 20 and can never exceed it. When the server can't finish all the work for a tick in the 50 milliseconds it's allotted, TPS falls below 20 and time itself slows down in the world — mobs move in slow motion, redstone lags, and hits stop registering. That's server-side lag, and no amount of internet upgrade fixes it.

Latency (ping, measured in milliseconds) is separate. A server holding a perfect 20.0 TPS can still feel awful if your packets take 200 ms to arrive. That's network lag, and no amount of server hardware fixes it.

## Fixing network lag (TPS is fine, ping is high)

If `/tps` shows a healthy 20.0 but the game still feels sluggish for you specifically, the server hardware is not your problem. Work through these in order.

**Check the physical distance.** This is the biggest lever most people ignore. A server in Frankfurt will feel bad from Los Angeles no matter how good the CPU is — light and routing overhead alone add 140-160 ms round trip across that distance. If your player base is regional, the server should be in or near that region. We cover this in depth in the [datacenter location guide](/guides/minecraft-server-datacenter-location/), including which hosts let you pick a location at checkout and which quietly put everyone in one facility.

**Test your own connection first.** Before blaming the host, run a ping test to the server IP from your machine (`ping your.server.ip` in a terminal). Compare it against your ping to a known-good site. If your home connection is spiking to a cloud gaming service too, the problem is on your end — WiFi interference, a saturated upstream, or your ISP — not the server.

**Ask about routing and DDoS filtering overhead.** Some hosts route all traffic through a scrubbing layer that adds latency even when you're not being attacked. Good ones ([Shockbyte](/reviews/shockbyte/), [Apex Hosting](/reviews/apex-hosting/), and [BisectHosting](/reviews/bisecthosting/) all advertise low-overhead filtering) keep this cost near zero. If your ping is high but stable and your route passes through a distant scrubbing center, that's the host's network design, and the only fix is a different provider or region.

**Rule out per-player issues.** If the server is smooth for everyone except one person, it's their connection, not the server. Have them test on mobile data versus WiFi — the difference is usually diagnostic.

## Fixing server-side lag (TPS is below 20)

This is where the money and the myths are. Low TPS means the server can't keep up with its own workload. The order of likely causes, from most to least common:

### 1. The CPU is too slow or too contended

Minecraft's main server tick runs on a **single thread**. That means the clock speed of one CPU core — not the number of cores, not the RAM — sets the ceiling on how much the server can do per tick. A 20-player Paper world will hold 20 TPS on a 5 GHz Ryzen core and struggle at 15 TPS on a contended 2.4 GHz cloud vCPU, with identical RAM and identical plugins.

This is why CPU disclosure is the buying signal we keep coming back to. [Server.pro](/reviews/server-pro/) is unusually honest here, splitting its fleet into labeled tiers — a weak EPYC 7351P (2.4 GHz base) on free and entry plans, a Ryzen 7 5800X on "Gaming", and a Ryzen 9 9950X3D on "Performance". You know exactly what core your tick loop lands on. [Shockbyte](/reviews/shockbyte/) runs a mix — newer nodes on Ryzen 9 7950X and EPYC 4465P, older ones on Intel Xeon E-2276G — and which you get isn't disclosed at checkout, which is exactly the uncertainty that produces "why is my server lagging" threads.

If your TPS is bad, RAM sits at 40-60%, and CPU is pegged near 100% on a single core in your panel's resource graph, you are CPU-constrained. More RAM will do nothing. Your options are a host with a faster disclosed CPU, or reducing the per-tick workload (the next three sections).

### 2. View-distance and simulation-distance are too high

This is the highest-impact free fix on the list. In `server.properties`:

- **`view-distance`** controls how many chunks the server loads and streams to each player. The default is 10. Every extra chunk of radius is more terrain to keep in memory and send over the wire, multiplied by every online player.
- **`simulation-distance`** controls how far out entities, redstone, and block ticks actually run. The default is 10.

Dropping `view-distance` to 6-7 and `simulation-distance` to 4-6 can cut tick time dramatically on a busy server, and most players genuinely never notice — you can't meaningfully interact with terrain 10 chunks away anyway. On a 20-player server this change alone often recovers several TPS. Do this before you spend a cent on upgrades.

### 3. Entities and hostile mob farms

Every mob, item frame, armor stand, dropped item, and hopper is work the server does every tick. The classic TPS killer is a mob farm — sometimes an intentional one, sometimes a mob-trap that filled up because nobody's collecting from it. Thousands of mobs crammed in a small area is thousands of AI pathfinding calculations per tick.

Spark's `/spark tps --entities` or a plugin like ClearLag will show you entity counts by type and chunk. Common culprits: giant animal pens, item-frame map walls, dropped-item accumulation near AFK farms, and villager breeders that got out of hand. Cap mob spawns in `bukkit.yml` (`spawn-limits`) and set a reasonable `merge-radius` for dropped items in `spigot.yml`.

### 4. A single misbehaving plugin or mod

One badly written plugin can eat an entire tick. Spark is built exactly for this — run `/spark profiler` for a few minutes under normal load, stop it, and read the report. It shows you, by percentage of tick time, which plugin and which method is the cost. It is genuinely the difference between guessing and knowing.

Common offenders: dynmap/BlueMap rendering on the main thread, CoreProtect logging with months of un-purged history, poorly optimized custom-item plugins, and anything doing synchronous database calls. For modded servers, worldgen mods and chunkloaders are the usual suspects — a quarry or a chunk-loading base can quietly keep hundreds of chunks resident and ticking.

### 5. Garbage-collection pauses (the one case where RAM matters)

If your heap is genuinely too small for your workload, Java's garbage collector runs constant, long pauses that show up in-game as periodic freezes — smooth, freeze, smooth, freeze. This is the *only* lag pattern that more RAM actually fixes, and you should confirm it before acting: Spark's memory view or your panel's RAM graph will show a sawtooth climbing to near-100% with GC events long enough to feel.

The fix is two-part: allocate enough heap (see the [RAM sizing guide](/guides/minecraft-server-ram/) for real numbers by server type), and use tuned GC flags. The community standard is **Aikar's flags**, a G1GC configuration that most decent managed hosts apply for you — but it's worth verifying in your startup command if you see pause-stutter on a server that's otherwise correctly sized. A 200-mod pack on default GC flags with a 10 GB heap will stutter; the same pack with Aikar's flags often won't.

## The upgrade decision: what to actually buy

Once you've diagnosed the real cause, the buying decision is straightforward and usually cheaper than people expect:

- **Network lag from distance** → move to a host with a datacenter near your players. Not a hardware upgrade at all. See the [location guide](/guides/minecraft-server-datacenter-location/).
- **CPU-constrained (100% one core, RAM fine)** → a host with a faster *disclosed* CPU, not a bigger plan on the same slow silicon. A 4 GB plan on a Ryzen 9 beats an 8 GB plan on a contended cloud core every time.
- **Config-constrained (view-distance, entities, one plugin)** → free. Fix the config and the farm before you pay anyone anything.
- **Genuinely out of RAM (GC sawtooth)** → the one case where a bigger plan is the right answer. Size it with the [RAM guide](/guides/minecraft-server-ram/).

The trap to avoid is the reflexive "buy more RAM" upgrade. It's the most-sold fix and the least-often-correct one, because hosts price by RAM and it's the easy number to upsell. Diagnose first with `/tps` and Spark, then buy the thing that matches the actual bottleneck. For side-by-side pricing and, crucially, which hosts disclose their CPUs, our [hosting comparison](/best-minecraft-server-hosting/) breaks down what you're really paying for at each tier.

## Quick reference: lag checklist

1. Run `/tps` or `/spark tps`. TPS 20.0 = network problem. TPS below 20 = server problem. Don't skip this step.
2. **Network:** check datacenter distance first, then your own connection, then the host's routing.
3. **Server-side:** check the panel resource graph. One core at 100% = CPU-bound. RAM sawtooth to 100% = memory-bound. Neither maxed = config/plugin.
4. Drop `view-distance` to 6-7 and `simulation-distance` to 4-6 — free, high impact.
5. Check entity counts with Spark; clear runaway mob farms and dropped items.
6. Run `/spark profiler` to find the one plugin eating your tick.
7. Only buy more RAM if you've *confirmed* GC pauses. Otherwise buy CPU disclosure, or fix the config.

A server that holds 20.0 TPS with low ping to your players is the goal, and most of the way there is free. The rest is buying the right spec, not the biggest one.
