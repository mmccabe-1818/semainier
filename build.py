#!/usr/bin/env python3
"""Merge events.json into template.html -> index.html.
Validates dates, drops past events, dedupes by (title, venue), sorts."""
import json, re, sys, datetime, pathlib

ROOT = pathlib.Path(__file__).parent
data = json.loads((ROOT / "events.json").read_text())
today = datetime.date.today()

def d(s):
    return datetime.date.fromisoformat(s)

seen, events, problems = set(), [], []
for e in data["events"]:
    try:
        s, en = d(e["start"]), d(e.get("end") or e["start"])
    except Exception as ex:
        problems.append(f"bad date: {e.get('title')}: {ex}"); continue
    if en < s:
        problems.append(f"end before start: {e['title']}"); continue
    if en < today:
        continue
    key = (e["title"].strip().lower(), e["venue"].strip().lower())
    if key in seen:
        continue
    seen.add(key)
    e["end"] = en.isoformat()
    e.setdefault("region", "marseille")
    e.setdefault("confidence", "medium")
    events.append(e)

events.sort(key=lambda e: (e["start"], e.get("time") or ""))
data["events"] = events
data["updated"] = datetime.date.fromisoformat(data.get("collected", today.isoformat())).strftime("%a %-d %b %Y")
nxt = today + datetime.timedelta(days=(7 - today.weekday()) % 7 or 7)
data["next_update"] = nxt.strftime("%a %-d %b")

payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = (ROOT / "template.html").read_text().replace("__DATA__", payload)
(ROOT / "index.html").write_text(html)
print(f"{len(events)} events written; {len(problems)} problems")
for p in problems:
    print("  !", p)
