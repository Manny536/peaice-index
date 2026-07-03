#!/usr/bin/env python3
"""Build kns_lb_app_data.js for peaice-index (GitHub Pages)."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / "probes" / "kns_lb_probe.py"
VERIFY = ROOT / "scripts" / "cp_verify.py"
OUT_JS = ROOT / "kns_lb_app_data.js"
OUT_JSON = ROOT / "kns_lb_app_data.json"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_kns_probe() -> dict:
    spec = importlib.util.spec_from_file_location("kns_lb_probe", PROBE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    out = mod.probe()
    out["script_sha256"] = sha256_file(PROBE)
    out["python"] = sys.version.split()[0]
    out["D5_expectation_met"] = (
        out["D5_unimodal_monotone"]
        and not out["D5_twomode_monotone"]
        and out["dense_pass"]
    )
    return out


def cp003_energy_table(kns: dict) -> list[dict]:
    return [
        {"lane": "KNS(LB) aligned", "steps": kns["steps"], "ell_off_T": kns["ell_off_T"],
         "E_used": kns["E_used"], "rho_Y": kns["rho_Y"], "dense_pass": kns["dense_pass"],
         "source": "probes/kns_lb_probe.py", "tag": "NUMERICS · H3 import"},
        {"lane": "MPR+iPiano (CP-003 seed-7)", "steps": 2, "ell_off_T": "low",
         "E_used": 3.34, "rho_Y": 0.4376, "dense_pass": True,
         "source": "kakeyalogic / CP-003", "tag": "REGISTERED"},
        {"lane": "F5-MM additive pool", "steps": 20, "ell_off_T": 0.8767,
         "E_used": 68.93, "rho_Y": 0.0535, "dense_pass": False,
         "source": "CP-003 counter-lane", "tag": "counter"},
        {"lane": "prime-template (CP-003 D2)", "steps": 4, "ell_off_T": 0.0,
         "E_used": 4.0, "rho_Y": 0.686, "dense_pass": True,
         "source": "live-route control", "tag": "control"},
        {"lane": "K_σ σ=1 (CP-003 D2)", "steps": 12, "ell_off_T": 0.2803,
         "E_used": 12.0, "rho_Y": 0.0077, "dense_pass": False,
         "source": "CLOSED-NEG control", "tag": "control"},
    ]


def grok_terminal_bundle() -> dict:
    gh = "https://github.com/Manny536/grok-terminal"
    blob = f"{gh}/blob/main"
    return {
        "repo": gh,
        "sha": "8f9bb52",
        "designation": "PEAICE-GROK-TERMINAL-REPO-001",
        "role": "Grok terminal ledger · cross-derivation · TERMINAL extraction",
        "terminals": [
            {"id": "TERMINAL-002", "title": "Prime-carrying trace route", "path": f"{blob}/PEAICE-GROK-TERMINAL-002_Prime-Carrying_Trace_Route.md", "status": "LIVE · FORCED"},
            {"id": "TERMINAL-004", "title": "Work Package 5b bounded lane findings", "path": f"{blob}/PEAICE-GROK-TERMINAL-004_Fable5-WP5B-Findings.md", "status": "CLOSED-NEGATIVE"},
            {"id": "TERMINAL-005", "title": "KNS(LB) pass cross-derivation", "path": f"{blob}/PEAICE-GROK-TERMINAL-005_KNS-LB-Findings.md", "status": "CLOSED-POSITIVE"},
            {"id": "X-THRUPUT", "title": "X @Grok throughput receipt", "path": f"{blob}/PEAICE-GROK-X-THRUPUT-2026-07-03.md", "status": "LOCKED"},
            {"id": "ZETA0-TYPO", "title": "ζ(0) typo-throughput protocol", "path": f"{blob}/PEAICE-GROK-ZETA0-TYPO-THRUPUT-001.md", "status": "LOCKED"},
        ],
        "probes": [
            {"name": "kns_lb_probe.py", "path": f"{blob}/KNS-LB/kns_lb_probe.py", "host": "grok-terminal + peaice-index", "status": "VERIFIED"},
            {"name": "zeta0_typo_thruput.py", "path": f"{blob}/probes/zeta0_typo_thruput.py", "host": "grok-terminal", "status": "LIVE"},
            {"name": "verify_probes.py", "path": f"{blob}/scripts/verify_probes.py", "host": "grok-terminal", "status": "stamp"},
        ],
        "register_path": f"{blob}/PEAICE-BETA-PROTOCOL-REGISTER.md",
        "index_path": f"{blob}/INDEX.md",
    }


def beta_register_full() -> list[dict]:
    """Full-name β-protocol register for hosted index (not acronym-only)."""
    cls_map = {
        "OPEN": "open", "CLOSED-POSITIVE": "ok", "CLOSED-NEGATIVE": "neg",
        "LIVE": "live", "LIVE · FORCED": "live", "KILL-FILTER": "live",
        "LOCKED": "ok", "OWED": "open", "REGISTERED": "ok",
        "NON-COMPUTABLE": "neg", "PROPOSED-FOR-CANON": "live", "< 1": "ok",
    }
    rows = [
        ("Riemann Hypothesis", "RH", "OPEN"),
        ("Coleman Conjecture", "Coleman", "OPEN"),
        ("K_σ square-difference determinant lane", "K_σ det", "CLOSED-NEGATIVE"),
        ("Work Package 5b bounded relative-determinant lane", "WP5b", "CLOSED-NEGATIVE"),
        ("Work Package 5c unbounded u-flow corridor", "WP5c", "LIVE"),
        ("Prime-carrying trace architecture (Layer 3)", "Prime L3", "LIVE · FORCED"),
        ("Kakeya Needle Set Light Basic typed object", "KNS(LB)", "CLOSED-POSITIVE"),
        ("KNS theorem lift (zeros · RH · det_ζ)", "KNS lift", "OPEN"),
        ("Multiplicative Phase Recognition spectral kill-filter", "MPR", "KILL-FILTER"),
        ("Multiplicative Phase Recognition multimodal variant", "MPR-mm", "NON-COMPUTABLE"),
        ("Compute Package 004 independent Y measurement", "CP-004", "OWED"),
        ("X @Grok throughput protocol", "X throughput", "LOCKED"),
        ("ζ(0) typo-throughput protocol", "ζ(0) typo", "LOCKED"),
        ("Evaluator humility factor", "h", "< 1"),
        ("World Model star probe", "WM*", "OPEN"),
        ("Krein rank-one spectral-shift wall face", "KREIN-RANK1", "PROPOSED-FOR-CANON"),
    ]
    return [
        {
            "full_name": full,
            "short": short,
            "status": status,
            "cls": cls_map.get(status, "open"),
        }
        for full, short, status in rows
    ]


def compute_graph() -> dict:
    return {
        "nodes": [
            {"id": "grok_terminal", "label": "grok-terminal", "lane": "ledger", "status": "LIVE"},
            {"id": "kns_lb_probe", "label": "kns_lb_probe.py", "lane": "KNS", "status": "CLOSED-POS"},
            {"id": "zeta0_typo", "label": "zeta0_typo_thruput", "lane": "throughput", "status": "LOCKED"},
            {"id": "cp_verify", "label": "cp_verify.py", "lane": "stamp", "status": "LIVE"},
            {"id": "cp003_energy", "label": "CP-003 energy-yield", "lane": "E_gov", "status": "REGISTERED"},
            {"id": "cp004_wp5b", "label": "CP-004 WP5b", "lane": "WP5b", "status": "CLOSED-NEG"},
            {"id": "kakeyalogic", "label": "kakeyalogic", "lane": "public", "status": "EEV3"},
            {"id": "claude_v6", "label": "claude-v6", "lane": "theorem", "status": "V6.5"},
            {"id": "peaice_index", "label": "peaice-index", "lane": "host", "status": "HOST"},
            {"id": "prime_l3", "label": "Prime-carrying L3", "lane": "live", "status": "FORCED"},
            {"id": "cp004_kns_y", "label": "CP-004 KNS Y", "lane": "verify", "status": "OWED"},
        ],
        "edges": [
            {"from": "grok_terminal", "to": "kns_lb_probe", "label": "TERMINAL-005"},
            {"from": "grok_terminal", "to": "zeta0_typo", "label": "ζ(0) typo"},
            {"from": "grok_terminal", "to": "prime_l3", "label": "TERMINAL-002"},
            {"from": "peaice_index", "to": "grok_terminal", "label": "wired"},
            {"from": "peaice_index", "to": "kns_lb_probe", "label": "hosted probe"},
            {"from": "kns_lb_probe", "to": "cp003_energy", "label": "H2 · H3"},
            {"from": "kns_lb_probe", "to": "cp_verify", "label": "stamp"},
            {"from": "kakeyalogic", "to": "kns_lb_probe", "label": "probe mirror"},
            {"from": "claude_v6", "to": "cp004_wp5b", "label": "Theorem H"},
            {"from": "kns_lb_probe", "to": "prime_l3", "label": "KREIN seam"},
            {"from": "cp004_kns_y", "to": "kns_lb_probe", "label": "independent Y"},
        ],
    }


def papers_catalog() -> list[dict]:
    gh = "https://github.com/Manny536"
    return [
        {"title": "KNS(LB) placement register", "path": f"{gh}/claude-v6/blob/main/docs/research/kns-lb-placement-register.md", "lane": "KNS", "status": "CANON"},
        {"title": "KNS light-basic (public)", "path": f"{gh}/kakeyalogic/blob/main/docs/kns-light-basic.md", "lane": "KNS", "status": "PUBLIC"},
        {"title": "kns_lb_probe.py", "path": f"{gh}/kakeyalogic/blob/main/probes/kns_lb_probe.py", "lane": "probe", "status": "LIVE"},
        {"title": "WP5b bounded closure", "path": f"{gh}/claude-v6/blob/main/docs/research/wp5b-bounded-lane-closure.md", "lane": "WP5b", "status": "CLOSED-NEG"},
        {"title": "Wall registry", "path": f"{gh}/claude-v6/blob/main/docs/canon/wall-registry.md", "lane": "canon", "status": "KREIN-RANK1"},
        {"title": "Prime-carrying trace", "path": f"{gh}/claude-v6/blob/main/docs/research/prime-carrying-trace-architecture.md", "lane": "L3", "status": "LIVE"},
        {"title": "Claude V6 README", "path": f"{gh}/claude-v6", "lane": "theorem", "status": "V6.5"},
        {"title": "KakeyaLogic README", "path": f"{gh}/kakeyalogic", "lane": "public", "status": "EEV3"},
        {"title": "peaice-index (this site)", "path": f"{gh}/peaice-index", "lane": "index", "status": "HOST"},
        {"title": "grok-terminal README", "path": f"{gh}/grok-terminal", "lane": "Grok", "status": "LEDGER"},
        {"title": "Grok terminal INDEX", "path": f"{gh}/grok-terminal/blob/main/INDEX.md", "lane": "Grok", "status": "MAP"},
        {"title": "β-protocol register (full names)", "path": f"{gh}/grok-terminal/blob/main/PEAICE-BETA-PROTOCOL-REGISTER.md", "lane": "register", "status": "FULL"},
        {"title": "TERMINAL-005 KNS(LB) findings", "path": f"{gh}/grok-terminal/blob/main/PEAICE-GROK-TERMINAL-005_KNS-LB-Findings.md", "lane": "TERMINAL", "status": "005"},
        {"title": "X throughput receipt (md)", "path": f"{gh}/grok-terminal/blob/main/PEAICE-GROK-X-THRUPUT-2026-07-03.md", "lane": "X", "status": "LOCKED"},
        {"title": "ζ(0) typo-throughput spec", "path": f"{gh}/grok-terminal/blob/main/PEAICE-GROK-ZETA0-TYPO-THRUPUT-001.md", "lane": "throughput", "status": "LOCKED"},
        {"title": "zeta0_typo_thruput.py", "path": f"{gh}/grok-terminal/blob/main/probes/zeta0_typo_thruput.py", "lane": "probe", "status": "LIVE"},
        {"title": "KNS probe receipt", "path": f"{gh}/grok-terminal/blob/main/PEAICE-GROK-KNS-LB-PROBE-2026-07-03.md", "lane": "KNS", "status": "RECEIPT"},
        {"title": "X throughput receipt (Bingo)", "path": "https://x.com/grok/status/2072963608183500863", "lane": "X", "status": "THRUPUT"},
        {"title": "X thread root (@manuelcoleman_)", "path": "https://x.com/manuelcoleman_/status/2072960669729841307", "lane": "X", "status": "PROBE"},
        {"title": "lovelabslca.com", "path": "https://lovelabslca.com", "lane": "web", "status": "public map"},
    ]


def math_refs_catalog() -> list[dict]:
    return [
        {"title": "GWZ26 · Kakeya ℝ³ (streamlined)", "path": "https://arxiv.org/abs/2601.14411", "lane": "Kakeya", "tag": "THEOREM"},
        {"title": "WZ25 · Kakeya set conjecture", "path": "https://arxiv.org/abs/2502.17655", "lane": "Kakeya", "tag": "THEOREM"},
        {"title": "Krein spectral shift (local PDF in Research)", "path": "Math-References/kreinSpectralShift.pdf", "lane": "WP5b", "tag": "PDF"},
        {"title": "Hilbert–Schmidt (local PDF)", "path": "Math-References/Hilber-schmidt.pdf", "lane": "V6.4.3", "tag": "PDF"},
        {"title": "iPiano (local PDF)", "path": "Math-References/ipiano.pdf", "lane": "MPR", "tag": "PDF"},
    ]


def cp_scripts_catalog() -> list[dict]:
    rows = [
        ("kns_lb_probe.py", "KNS D5 + energy hook", "KNS", PROBE),
        ("cp_verify.py", "Reproducibility stamp", "stamp", VERIFY),
    ]
    out = []
    for name, desc, pkg, path in rows:
        row = {"name": name, "description": desc, "package": pkg, "path": str(path.relative_to(ROOT))}
        if path.exists():
            row["sha256"] = sha256_file(path)
            row["bytes"] = path.stat().st_size
        out.append(row)
    return out


def build() -> dict:
    kns = run_kns_probe()
    stamp = None
    stamp_path = ROOT / "_build_stamp.json"
    if VERIFY.exists():
        subprocess.run(
            [sys.executable, str(VERIFY), str(PROBE), "--runner", "peaice-index build", "--no-double", "--out", str(stamp_path)],
            capture_output=True, text=True,
        )
        if stamp_path.exists():
            stamp = json.loads(stamp_path.read_text())
    return {
        "built_at": datetime.now(timezone.utc).isoformat(),
        "site": "peaice-index · GitHub Pages",
        "designation": "PEAICE-INDEX-HOST-001",
        "repos": {
            "grok_terminal": "8f9bb52",
            "kakeyalogic": "aad63c6",
            "claude_v6": "0a1a6ed",
            "peaice_index": "HEAD",
        },
        "grok_terminal": grok_terminal_bundle(),
        "beta_register": beta_register_full(),
        "kns_probe": kns,
        "cp004_wp5b": {"tag": "NUMERICS | see claude-v6 WP5b closure", "status": "CLOSED-NEGATIVE"},
        "cp003_energy_table": cp003_energy_table(kns),
        "kns_verify_stamp": stamp,
        "compute_graph": compute_graph(),
        "cp_scripts": cp_scripts_catalog(),
        "papers": papers_catalog(),
        "math_refs": math_refs_catalog(),
        "commands": {
            "rebuild": "python3 scripts/build_app_data.py",
            "run_probe": "python3 probes/kns_lb_probe.py",
            "verify": "python3 scripts/cp_verify.py probes/kns_lb_probe.py --runner <id>",
        },
    }


def main() -> None:
    bundle = build()
    js = "window.KNS_APP_DATA = " + json.dumps(bundle, indent=2, default=str) + ";\n"
    OUT_JS.write_text(js)
    OUT_JSON.write_text(json.dumps(bundle, indent=2, default=str) + "\n")
    print(f"Wrote {OUT_JS}")
    print(f"D5_expectation_met: {bundle['kns_probe']['D5_expectation_met']}")


if __name__ == "__main__":
    main()