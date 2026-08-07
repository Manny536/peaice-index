# MPR Formal Core — public pointer

**Designation:** `PEAICE-MPR-FORMAL-CORE-001`  
**Date:** 2026-08-07  
**State:** FORMAL DEFINITION · satisfaction OPEN · kill-filter operational  
**Discipline:** RH OPEN · Coleman OPEN · `h < 1` · PASS non-promoting

## Public summary

Multiplicative Phase Recognition (MPR) is the program’s **spectral kill-filter** and now has a typed formal core:

```text
MPR = prime-power arithmetic recovered from determinant phase
```

Relative phase \(\mathcal M_\tau\) extracted from a trace-class pair \((A_\tau,D_\tau)\) is recognized when it equals the prime-power target \(\mu_\times\) in the dual of even test functions. That **equality criterion is FORMAL**. Whether any live DDATL operator satisfies it remains **OPEN**.

Operational verdicts stay under the kill-filter:

```text
FAIL → construction killed
PASS → survives screen only · certifies nothing about zeros · RH OPEN
```

## Layers (do not collapse)

| Layer | Status |
|-------|--------|
| Kill-filter (gates MPR-1…8) | **KILL-FILTER** |
| \(J_{\mathrm{MPR}}\) product form | **REGISTERED supporting** |
| \(\mathcal M_\tau=\mu_\times\) | **FORMAL definition** |
| Live operator satisfaction | **OPEN** |
| Multimodal MPR | **NON-COMPUTABLE** |
| MPR+iPiano energy class | **REGISTERED** ≠ spectral PASS |

## Source map

| Surface | Role |
|---------|------|
| [TERMINAL-007](https://github.com/Manny536/grok-terminal/blob/main/PEAICE-GROK-TERMINAL-007_MPR-Formal-Core.md) | Full formal core receipt |
| [β-protocol register](https://github.com/Manny536/grok-terminal/blob/main/PEAICE-BETA-PROTOCOL-REGISTER.md) | §10 kill-filter · §24 MPR-core |
| [mpr_formal_core.py](https://github.com/Manny536/grok-terminal/blob/main/probes/mpr_formal_core.py) | Definition-hygiene probe |
| [TERMINAL-002](https://github.com/Manny536/grok-terminal/blob/main/PEAICE-GROK-TERMINAL-002_Prime-Carrying_Trace_Route.md) | Prime-carrying live route |

## Firewall

```text
MPR PASS ≠ RH progress
definition ≠ satisfaction
q_m ≠ ρ_Y
AUTH-DETECT ≠ MPR
```

## Centerline

```text
definition ↑ · promotion — · existence ○ · kill-filter ■
```
