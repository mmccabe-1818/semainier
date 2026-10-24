# Semainier

What's on in Marseille this week. One page, rebuilt every Monday.

- `index.html` — the published page (generated; do not edit by hand)
- `template.html` — page markup, styles and client script; `__DATA__` is replaced at build time
- `events.json` — the listings. `collected` is the date the listings were gathered
- `build.py` — validates `events.json`, drops expired entries, writes `index.html`
- `sources.json` — the fixed roster of venue and aggregator pages checked every week
- `festivals.json` — recurring festivals and their usual windows
- `missed.md` — things the scan missed; the next run reads it

## Weekly run

1. Fetch every URL in `sources.json`; for each festival in `festivals.json` whose window is within six weeks, find this year's dates.
2. Merge into `events.json`: add new entries, update changed dates, keep anything still running. An entry needs two sources, or it gets `"confidence": "low"` (shown as *check* on the page).
3. Diff against the previous `events.json`; write the differences to `changelog` in `events.json`.
4. Read `missed.md`; add any new source or festival named there.
5. `python3 build.py`, commit, push. GitHub Pages redeploys within a minute.

## Page rules

- *This week*: dated events in the next seven days, plus long-run shows that open or close this week.
- *Coming up*: dated events in the following five weeks.
- *On now*: anything running 21 days or more, sorted by closing date; "closes soon" within 14 days.
- *Further afield*: entries with `"region": "afield"`.
- Categories: exhibition→Art, theatre, dance, music (incl. opera, classical), cinema, talk, festival, family.
