# Misses log

One line per thing the scan missed or got wrong. The next weekly run reads this file, adds the source, and ticks the line.

| Date noted | What was missed | Why | Fix |
|---|---|---|---|
| 2026-10-24 | ✓ CinéHorizontes (Spanish cinema festival, Nov) | Not on any roster source until two weeks out | Added to festivals.json; 2026 edition actually ran 8–16 Oct, window moved to October (2026-10-26) |
| 2026-10-24 | ✓ Openings and last days of long-run shows absent from *This week* | Rule sent every run ≥21 days to *On now* only | Page now shows "opens" / "last day" rows in *This week* |
| 2026-10-24 | ✓ Musée Cantini "Par une langue échappée": note described the wrong show (generic Picasso/Matisse blurb instead of the new hang around Marseille and its diasporas) | Source link was the museum homepage; note taken from a tourist-office summary | Entry corrected. Rule: link must be the event's own page; note must come from that page or a press write-up, otherwise "check" |
| 2026-10-26 | Mucem November agenda (talks, cinema, concerts after Averroès) | mucem.org/en/agenda renders no listings to the fetcher; /programme returns a stale cache | Try mucem.org/fr/agenda via a search hit, or the monthly press "programme" PDF |
| 2026-10-26 | Friche la Belle de Mai agenda after 9 Nov (music, talks) | lafriche.org/agenda/?page=2 stops at 9 Nov | Fetch lafriche.org/agenda/?page=3 and ?page=4, or the month filter |
| 2026-10-26 | Opéra de Marseille / Odéon 27 Nov–6 Dec (foyer concerts 29 Nov, 6 Dec) and Les Théâtres season pages 2–4 | Only page 1 of each listing read | Paginate both listings |
| 2026-10-26 | Théâtre de l'Œuvre, Montévidéo, Toursky, Ballet National de Marseille, Théâtre Nono not checked | Stage scan ran out of fetch budget | Toursky added to sources.json; give the stage scan its own budget for these |
| 2026-10-26 | Le Molotov, Cabaret Aléatoire, Espace Julien, Les Variétés, Alhambra, Gyptis own sites unreachable (provenance refusals) | WebFetch only accepts URLs surfaced by a WebSearch in the same session | Search "<venue> <mois> 2026" first; note added to sources.json |
| 2026-10-26 | PriMed 2026 dates (likely late Nov–early Dec), Dansem 2026, Image de Ville Marseille dates | No announcement found | Re-search next run; festivals.json notes updated |
| 2026-10-26 | Mucem "Mayotte, Maoré" announced for 18 Nov 2026 | Reported postponed with no new date (Mayotte Hebdo, Sep 2026) | Not listed; re-check |
| 2026-10-26 | Frac Sud, Fondation Vasarely, Hôtel des Arts Toulon, MO.CO: what opens after mid-November | No new show announced on sources reached (Frac next show 30 Jan 2027) | Re-check next run |
