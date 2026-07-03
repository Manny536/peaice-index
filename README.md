# peaice-index

**PeAIce program index** — hosted interactive map for KNS(LB), compute receipts, and canon links.

**Designation:** `PEAICE-INDEX-HOST-001`  
**Maintained by:** Grok terminal (PeAIce instance) · Love Labs LCA  
**Discipline:** RH **OPEN** · Coleman **OPEN** · `h < 1` · no proof claimed

## Live site

GitHub Pages: **https://manny536.github.io/peaice-index/**

## What this is

- **index.html** — KNS(LB) light thought-probe UI (fan/Perron viz, probe receipt, CP graph, papers, math refs)
- **kns_lb_app_data.js** — live bundle from `scripts/build_app_data.py`
- **probes/kns_lb_probe.py** — deterministic KNS gate probe (stdlib only)
- **scripts/cp_verify.py** — reproducibility stamp harness

## Rebuild data

```bash
python3 scripts/build_app_data.py
python3 probes/kns_lb_probe.py   # expect exit 0
```

## Upstream canon repos

| Repo | Role |
|------|------|
| [claude-v6](https://github.com/Manny536/claude-v6) | Theorem-facing ledger · V6.5 |
| [kakeyalogic](https://github.com/Manny536/kakeyalogic) | Public EEV3 / L²_C · probes |

## Registered state (July 2026)

```text
K_σ CLOSED-NEGATIVE · WP5b CLOSED-NEGATIVE
KNS(LB) typed CLOSED-POSITIVE · theorem lift OPEN
Prime-carrying LIVE·FORCED · CP-004 OWED
```

PeAIce files ≠ automatic canon.