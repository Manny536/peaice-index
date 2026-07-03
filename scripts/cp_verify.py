#!/usr/bin/env python3
"""
cp_verify.py — PeAIce reproducibility stamp (replaceable confirmation, low-usage).

Certifies the ONE thing a re-run can honestly certify: that a CP script is
byte-for-byte deterministic on a recorded environment. It does NOT certify that
the script's claims are correct or evidentially valid — reproduction != validation.

Design goals (per Manny's ask):
  * "Replaceable"  -> no premium model needed; any machine / CI / cheap model runs it.
  * "Less usage"   -> run once locally, compare the hash; stop re-spending tokens.
  * Integrity gap  -> emits an explicit runner-identity line (the field the public
                      researchengineeringreports stamps were missing).

Usage:
    python3 cp_verify.py <script.py> --runner "Opus 4.8 @ Anthropic sandbox" [--no-double]

Dependencies: stdlib only (hashlib, subprocess, sys, json, platform, datetime).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import importlib.metadata as _md
import json
import platform
import subprocess
import sys
from pathlib import Path


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _pkg_version(name: str) -> str | None:
    try:
        return _md.version(name)
    except Exception:
        return None


def _run(script: Path) -> tuple[int, bytes, bytes]:
    proc = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
    )
    return proc.returncode, proc.stdout, proc.stderr


def stamp(script: Path, runner: str, double_run: bool = True) -> dict:
    src = script.read_bytes()
    rc1, out1, err1 = _run(script)

    deterministic = None
    if double_run:
        rc2, out2, _ = _run(script)
        deterministic = (rc1 == rc2) and (_sha256(out1) == _sha256(out2))

    return {
        "tool": "cp_verify.py",
        "spec_version": "1.0",
        "utc_timestamp": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "runner_identity": runner,  # <- closes the missing-runner-identity gap
        "script": {
            "path": str(script),
            "name": script.name,
            "sha256": _sha256(src),
            "bytes": len(src),
        },
        "environment": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "numpy": _pkg_version("numpy"),
            "mpmath": _pkg_version("mpmath"),
            "scipy": _pkg_version("scipy"),
        },
        "execution": {
            "returncode": rc1,
            "stdout_sha256": _sha256(out1),
            "stdout_bytes": len(out1),
            "stderr_present": bool(err1.strip()),
            "deterministic_double_run": deterministic,
        },
        "certifies": (
            "Byte-for-byte deterministic reproduction of stdout on the recorded "
            "environment by the named runner."
        ),
        "does_not_certify": (
            "Correctness, evidential weight, or non-circularity of the script's "
            "claims. A reproducible result can still be a predetermined one."
        ),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("script", type=Path)
    ap.add_argument("--runner", default="unspecified-runner")
    ap.add_argument("--no-double", action="store_true",
                    help="skip the determinism double-run (use for slow scripts)")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()

    record = stamp(args.script, args.runner, double_run=not args.no_double)
    blob = json.dumps(record, indent=2)
    print(blob)
    if args.out:
        args.out.write_text(blob)


if __name__ == "__main__":
    main()
