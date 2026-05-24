# Minecraft Hosting Glossary

Plain-English definitions of the terms you'll see in [our provider reviews](https://gamehostingguides.com/reviews/) and across hosting product pages. Sorted alphabetically.

## Aikar's Flags

A widely-used set of JVM tuning flags developed by the Paper team to reduce garbage-collection pauses on Minecraft servers. Most modern Minecraft hosts apply Aikar's flags by default; if you self-host, applying them can noticeably smooth out tick rate on servers with 8 GB+ of RAM.

## Backup

A point-in-time copy of your server's world, plugin configs, and player data. Most managed Minecraft hosts include 1–3 automatic backups; serious operators want daily backups with at least 7 days of retention. Always verify what's actually included rather than trusting "automatic backups" as a feature label.

## Bedrock Edition

The version of Minecraft for mobile, console, and Windows 10/11. Written in C++, uses 2-4× less RAM per player than [Java Edition](#java-edition), and uses different server software (Bedrock Dedicated Server, PocketMine, NukkitX). See our [Java vs Bedrock guide](https://gamehostingguides.com/guides/java-vs-bedrock-minecraft-servers/) for the hosting implications.

## BungeeCord

A proxy server that lets you connect multiple Minecraft servers as one network — players can switch between a lobby, survival, and minigames servers seamlessly. BungeeCord is a "proxy" that sits in front of "backend" servers, and it needs much less RAM (512 MB – 1 GB) than the backends themselves.

## CPU clock speed

The frequency at which a CPU core runs, measured in GHz. **For Minecraft hosting this matters far more than core count** because Minecraft's main game-loop is single-threaded — one fast core beats many slow ones. A disclosed Ryzen 7 7700 at 4.9 GHz boost will outperform an undisclosed "high-clock" budget CPU every time.

## Control panel

The web UI you use to manage your server: start/stop, edit config files, upload mods, view logs. The three you'll see most often:
- **Multicraft** — the legacy industry standard, used by Apex, Shockbyte, and many others
- **Pterodactyl** — modern open-source panel with good UX and resource visualization
- **Custom panels** — Nodecraft's NodePanel, BisectHosting's custom UI, etc.

## DDoS protection

Mitigation against distributed denial-of-service attacks (someone trying to crash your server with traffic flood). Reputable Minecraft hosts include layer-4 DDoS protection at the network edge. Layer-7 protection (against Minecraft-protocol attacks) is rarer but more valuable for high-profile servers.

## Dedicated core / dedicated CPU

A guarantee that a specific physical CPU core is reserved for your server only, with no "noisy neighbor" competing for cycles. Stands in contrast to **shared CPU** (the common budget-host model) where multiple customers' servers share the same cores. Dedicated cores cost more but give more predictable TPS.

## ECC RAM

Error-correcting memory that detects and corrects single-bit memory errors automatically. Rare at budget Minecraft hosting prices because it costs more than consumer-grade RAM. Useful for modpack servers that have known memory-corruption-sensitive issues. [ServerPrism](https://gamehostingguides.com/reviews/serverprism/) is the only host we've reviewed at sub-$5/mo entry pricing that uses ECC RAM by default.

## Forge

The most widely-used modding platform for Java Minecraft. Forge-modded servers need more RAM than vanilla — typically 6-10 GB for a 30-mod pack at 10-20 players. Note that Forge versions are tied to specific Minecraft versions.

## Fabric

A newer, lighter alternative to Forge for Minecraft modding. Many "performance" mods (Sodium, Iris, Lithium) are Fabric-only. Server RAM requirements are similar to Forge, but Fabric tends to have less mod compatibility for traditional gameplay modpacks.

## Geyser

A plugin that lets Java Edition Minecraft servers accept Bedrock Edition clients (mobile, console). Combined with Floodgate for auth, it's the standard way to run a cross-platform Minecraft server in 2026.

## Java Edition

The original Minecraft, written in Java. Required for mods (Forge, Fabric) and plugins (Spigot, Paper, Purpur). Heavier on RAM than Bedrock. Most "Minecraft hosting" providers default to Java Edition.

## Modpack

A bundled collection of mods (sometimes 50-500+) distributed as a single installable package. CurseForge, Modrinth, FTB (Feed The Beast), Technic, and ATLauncher are the major distribution platforms. Large modpacks need 6 GB+ of RAM and benefit heavily from high-clock CPUs.

## NVMe

A storage protocol that runs over PCIe, dramatically faster than SATA SSDs. Modern Minecraft hosts should all be using NVMe for chunk loading and world saves. SATA SSD is acceptable for vanilla; NVMe matters more for modded servers and large worlds. PCIe Gen4 NVMe (used by [ServerPrism](https://gamehostingguides.com/reviews/serverprism/) and others) is the current state of the art.

## Paper

A high-performance fork of Spigot/Bukkit. Most production Minecraft servers run Paper for the performance and configurability. Generally the recommended starting point for plugin servers.

## Plugin

A server-side modification that doesn't require client mods to use (different from a mod in the Forge/Fabric sense). Most plugins target Spigot, Paper, or Bukkit APIs. Plugin servers can run heavier than vanilla (typically 2× RAM) but lighter than modded.

## Proxy

A server that routes player connections to backend Minecraft servers without itself hosting any game state. [BungeeCord](#bungeecord) and Velocity are the two common proxies. Proxies enable network-style server architectures.

## Pterodactyl

An open-source server management panel used by many newer Minecraft hosts (BisectHosting, CloudNord, ServerPrism, etc.). Generally considered more modern and developer-friendly than Multicraft. Lets you do things like view live resource graphs, edit any file in the file manager, and create sub-users with scoped permissions.

## RAM allocation

The amount of memory your Minecraft server can use. For Java Edition, this needs to be allocated to the JVM at startup (you can't dynamically grow it). For sizing: see our [RAM guide](https://gamehostingguides.com/guides/minecraft-server-ram/) — short version: 2 GB for 5-player vanilla, 4 GB for plugin servers, 6-10 GB+ for modded.

## Slot / player slot

The maximum number of simultaneous players allowed on your server. Some hosts price by slot count (capped); others sell RAM-based plans where you can set slots yourself. Slot caps are largely artificial — RAM and CPU are the actual physical constraints.

## SLA (Service Level Agreement)

A contractual promise about uptime, support response time, and remediation if those promises are broken. Most budget Minecraft hosts don't publish a real SLA. Production server operators should ask for one or assume "no SLA" by default.

## Spigot

A Minecraft server fork that supports plugins via the Bukkit API. Predecessor to [Paper](#paper); most modern operators run Paper instead because it's faster, but the Spigot API name is still in common use.

## TPS (Ticks Per Second)

Minecraft's internal game-loop rate, targeted at 20 TPS (one tick every 50 ms). Below 20 TPS the game world runs in slow motion — mobs move slower, plant growth lags, redstone fires late. TPS is the single best signal of server health. Use the `/tps` command (Paper) or a plugin like Spark to monitor.

## Velocity

A modern proxy server, replacing [BungeeCord](#bungeecord) in many networks. Built by the PaperMC team. Same idea (route players between backend servers) but better performance and a more modern plugin API. Most new Minecraft networks use Velocity rather than BungeeCord in 2026.

## Vanilla

Plain Minecraft with no mods or plugins. Vanilla servers are the lightest workload — even a 10-player vanilla server runs comfortably on 2-4 GB of RAM.

## Whitelist

A list of player usernames allowed to join a server. Standard practice for private/friends servers, ignored by most public communities. Set with `/whitelist add <name>` and `/whitelist on` on a server console.

---

## See also

- [Best Minecraft Server Hosting 2026 — comparison](https://gamehostingguides.com/best-minecraft-server-hosting/)
- [How much RAM does a Minecraft server need?](https://gamehostingguides.com/guides/minecraft-server-ram/)
- [Java vs Bedrock servers — hosting implications](https://gamehostingguides.com/guides/java-vs-bedrock-minecraft-servers/)
- [Choosing a datacenter location](https://gamehostingguides.com/guides/minecraft-server-datacenter-location/)
- [Methodology](./Methodology)
