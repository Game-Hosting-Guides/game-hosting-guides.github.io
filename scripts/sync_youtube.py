#!/usr/bin/env python3
"""
Sync the latest videos from a YouTube channel's RSS feed into the Jekyll
_videos/ collection as companion landing pages.

Idempotent: only writes a file when content actually changes.

Manual edits are preserved: if a page contains the marker
"<!-- manual-edit -->" anywhere in its body, the script skips it.

Usage: python scripts/sync_youtube.py
"""

from __future__ import annotations

import html
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.request import Request, urlopen

CHANNEL_ID = "UCSsY8OOb3U70RSdogaJYmag"
CHANNEL_HANDLE = "GameHostingGuides"
RSS_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

REPO_ROOT = Path(__file__).resolve().parent.parent
VIDEOS_DIR = REPO_ROOT / "_videos"

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}

# Map review slug → (display name, lowercase keywords to search in video text).
REVIEW_PROVIDERS: dict[str, tuple[str, list[str]]] = {
    "apex-hosting":    ("Apex Hosting",   ["apex hosting", "apexhost", " apex "]),
    "shockbyte":       ("Shockbyte",      ["shockbyte"]),
    "bisecthosting":   ("BisectHosting",  ["bisect"]),
    "hostinger":       ("Hostinger",      ["hostinger"]),
    "nodecraft":       ("Nodecraft",      ["nodecraft"]),
    "mcprohosting":    ("MCProHosting",   ["mcprohosting", "mcpro"]),
    "serverprism":     ("ServerPrism",    ["serverprism"]),
    "cloudnord":       ("CloudNord",      ["cloudnord"]),
    "server-pro":      ("Server.pro",     ["server.pro", "server pro"]),
}


def clean_description(desc: str) -> str:
    """Drop hashtag-spam and URL-only lines; collapse blank runs."""
    if not desc:
        return ""
    keep: list[str] = []
    for line in desc.split("\n"):
        stripped = line.strip()
        if not stripped:
            keep.append("")
            continue
        tokens = stripped.split()
        hashy = sum(1 for t in tokens if t.startswith(("#", "http")))
        if tokens and hashy / len(tokens) > 0.55:
            continue
        keep.append(line)
    out = "\n".join(keep).strip()
    return re.sub(r"\n{3,}", "\n\n", out)


def extract_summary(clean_desc: str, max_chars: int = 500) -> str:
    """First paragraph(s) up to ~max_chars."""
    if not clean_desc:
        return ""
    out = ""
    for para in clean_desc.split("\n\n"):
        if out and len(out) + len(para) > max_chars:
            break
        out = (out + "\n\n" + para).strip()
    return out


def find_related_reviews(title: str, desc: str) -> list[tuple[str, str]]:
    haystack = (title + " " + (desc or "")).lower()
    return [
        (slug, name)
        for slug, (name, keywords) in REVIEW_PROVIDERS.items()
        if any(kw in haystack for kw in keywords)
    ]


def best_effort_transcript(video_id: str) -> str | None:
    """Optional: fetch auto-captions. Silently no-op if lib missing or fetch fails."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi  # type: ignore
    except ImportError:
        return None
    try:
        segments = YouTubeTranscriptApi.get_transcript(
            video_id, languages=["en", "en-US", "en-GB"]
        )
    except Exception as e:
        print(f"  Transcript fetch failed for {video_id}: {e!r}")
        return None
    text = " ".join(s.get("text", "").replace("\n", " ") for s in segments)
    return re.sub(r"\s+", " ", text).strip() or None


def yaml_escape(value: str) -> str:
    """Quote a string as a YAML double-quoted scalar."""
    escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return f'"{escaped}"'


def render_front_matter(fm: dict) -> str:
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        elif isinstance(v, (int, float)):
            lines.append(f"{k}: {v}")
        elif isinstance(v, list):
            lines.append(f"{k}: {json.dumps(v)}")
        else:
            lines.append(f"{k}: {yaml_escape(str(v))}")
    lines.append("---\n")
    return "\n".join(lines)


def render_body(entry: dict, summary: str, related: list[tuple[str, str]],
                transcript: str | None) -> str:
    parts: list[str] = []

    if summary:
        parts.append("## The 30-second version\n\n" + summary)

    video_id = entry["video_id"]
    is_short = entry["is_short"]
    embed_url = f"https://www.youtube.com/embed/{video_id}"
    embed_class = "video-embed short" if is_short else "video-embed"
    iframe = (
        f'<div class="{embed_class}">\n'
        f'<iframe src="{embed_url}" '
        f'title="{html.escape(entry["title"])}" '
        f'frameborder="0" '
        f'allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
        f'allowfullscreen loading="lazy"></iframe>\n'
        f"</div>"
    )
    parts.append(iframe)

    if related:
        parts.append(
            "## Hosting providers mentioned\n\n"
            + "\n".join(f"- [{name} review](/reviews/{slug}/)" for slug, name in related)
        )

    if transcript:
        parts.append("## Transcript\n\n" + transcript)

    parts.append(
        f'<p><a href="{entry["link"]}" rel="noopener" target="_blank">'
        f"Watch on YouTube &rarr;</a></p>"
    )
    return "\n\n".join(parts)


def upsert_video(entry: dict) -> bool:
    video_id = entry["video_id"]
    out_path = VIDEOS_DIR / f"{video_id}.md"

    if out_path.exists() and "<!-- manual-edit -->" in out_path.read_text(encoding="utf-8"):
        print(f"  Skipping {video_id} (manual-edit marker present)")
        return False

    clean_desc = clean_description(entry["description"])
    summary = extract_summary(clean_desc)
    related = find_related_reviews(entry["title"], clean_desc)
    transcript = best_effort_transcript(video_id)

    description_meta = (summary or entry["title"]).replace("\n", " ").strip()
    if len(description_meta) > 155:
        description_meta = description_meta[:152].rstrip() + "…"

    fm = {
        "title": entry["title"],
        "description": description_meta,
        "video_id": video_id,
        "video_url": entry["link"],
        "video_type": "short" if entry["is_short"] else "video",
        "thumbnail": entry["thumbnail"],
        "published": entry["published"][:10],
        "last_updated": entry["updated"][:10],
        "channel_name": "Game Hosting Guides",
        "channel_url": f"https://www.youtube.com/@{CHANNEL_HANDLE}",
    }
    if related:
        fm["mentioned_providers"] = [name for _, name in related]

    body = render_body(entry, summary, related, transcript)
    content = render_front_matter(fm) + "\n" + body + "\n"

    if out_path.exists() and out_path.read_text(encoding="utf-8") == content:
        return False

    out_path.write_text(content, encoding="utf-8")
    print(f"  Wrote {out_path.relative_to(REPO_ROOT)}")
    return True


def fetch_rss() -> bytes:
    req = Request(
        RSS_URL,
        headers={
            "User-Agent": "GameHostingGuidesBot/1.0 (+https://game-hosting-guides.github.io)"
        },
    )
    with urlopen(req, timeout=30) as resp:
        return resp.read()


def parse_entries(xml_bytes: bytes) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    out: list[dict] = []
    for e in root.findall("atom:entry", NS):
        video_id = e.findtext("yt:videoId", default="", namespaces=NS).strip()
        if not video_id:
            continue
        link_el = e.find("atom:link", NS)
        link = link_el.get("href") if link_el is not None else ""
        media_group = e.find("media:group", NS)
        description = ""
        thumbnail = ""
        if media_group is not None:
            description = media_group.findtext("media:description", default="", namespaces=NS) or ""
            thumb_el = media_group.find("media:thumbnail", NS)
            if thumb_el is not None:
                thumbnail = thumb_el.get("url", "")
        out.append({
            "video_id": video_id,
            "title": (e.findtext("atom:title", default="", namespaces=NS) or "").strip(),
            "published": (e.findtext("atom:published", default="", namespaces=NS) or "").strip(),
            "updated": (e.findtext("atom:updated", default="", namespaces=NS) or "").strip(),
            "link": link,
            "description": description,
            "thumbnail": thumbnail,
            "is_short": "/shorts/" in link,
        })
    return out


def main() -> int:
    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Fetching {RSS_URL}")
    xml_bytes = fetch_rss()
    entries = parse_entries(xml_bytes)
    print(f"Parsed {len(entries)} entries")
    changed = 0
    for entry in entries:
        if upsert_video(entry):
            changed += 1
    print(f"Done. {changed} file(s) created or updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
