# CS-EQ-Teensy4_1 — SSL-Style Digital Equalizer

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-signal-8CAAE6?logo=scipy&logoColor=white)
![Target](https://img.shields.io/badge/Target-Teensy%204.1%20(ARM%20Cortex--M7)-ee6b2d)
![Status](https://img.shields.io/badge/status-work%20in%20progress-yellow)

A from-scratch digital audio equalizer modelled on the classic **SSL channel-strip EQ**,
designed to run on a **Teensy 4.1** (600 MHz ARM Cortex-M7) microcontroller.

The engineering approach is **prototype-then-port**: every filter is first derived,
implemented, and validated in Python with `numpy` / `scipy.signal`, then reduced to a
discrete difference equation whose coefficients can be dropped straight into a real-time
C++ audio loop on the Teensy.

The project applies control-systems theory from **ETH Zürich — *Control Systems 1*** to a
practical audio-engineering problem: Laplace-domain transfer functions `H(s)`, pole/cutoff
behaviour, discretization, and difference equations are the same tools used here to design
and run the EQ filters. *("CS-EQ" = **C**ontrol-**S**ystems **EQ**.)*

> **Status:** Early *Learning Basics* phase — DSP fundamentals are being built and
> validated in Python before the embedded port. See the [roadmap](#roadmap) below.

---

## Why this project

Hardware EQs cost hundreds of euros and hide their maths. The goal here is to
**understand digital filtering from first principles** — not by calling a black-box
library, but by deriving the recurrence relations by hand, then cross-checking them
against `scipy.signal`, and finally running them on bare-metal embedded hardware where
sample rate and loop timing actually matter.

---

## Repository structure

Phase-1 prototyping code lives under `Learning Basics/`:

| File | Description |
|------|-------------|
| `Learning Basics/SineWaveGenerator.py` | Generates and superimposes sine waves of different frequencies; plots the components and their sum with `matplotlib`. Foundation for building and inspecting test signals. |
| `Learning Basics/Core_IRR_Filter.py` | First-principles **single-pole recursive IIR filter** implemented by hand: `y[i] = a·x[i] + (1−a)·y[i−1]` (an exponential moving average / one-pole low-pass), with a high-pass derived by spectral subtraction (`x − lp`). *Work in progress.* |
| `Learning Basics/scipy_basics.py` | Designs a continuous-time first-order low-pass `H(s) = ω₀ / (s + ω₀)` (ω₀ = 2π·5 rad/s) with `scipy.signal.TransferFunction`, discretizes it with the **bilinear / Tustin transform** (`to_discrete`, generalized bilinear, α = 0.5) at fs = 1 kHz, and extracts the **difference-equation coefficients** (bᵢ, aᵢ) — exactly the artefact needed to port a filter to a fixed-rate Teensy loop. |
| `Learning Basics/Ressources/` | Reference material — the SciPy `signal` v1.17.0 manual (PDF). |

---

## DSP concepts explored

- **Signal generation & superposition** — building composite test signals from sinusoids.
- **Single-pole IIR filtering** — the exponential-moving-average recurrence, the
  low-pass ↔ high-pass relationship, and the effect of the smoothing coefficient.
- **Continuous → discrete design** — going from a Laplace-domain transfer function
  `H(s)` to a digital filter via the bilinear (Tustin) transform.
- **Difference equations** — reducing a discrete transfer function to the
  `y[n] = Σ bᵢ·x[n−i] − Σ aᵢ·y[n−i]` form that a microcontroller can execute per sample.

---

## Roadmap

| Phase | Goal | Status |
|-------|------|--------|
| 1. Learning Basics | Core DSP in Python: signal generation, hand-rolled IIR, transfer-function discretization | 🔄 In progress |
| 2. Filter Design | Design the EQ bands (low shelf, high shelf, peaking/bell) and validate frequency response with plots | ⏳ Planned |
| 3. Teensy Prototype | Port validated filter coefficients to C++ on the Teensy 4.1 | ⏳ Planned |
| 4. Audio I/O | Wire up ADC/DAC or an I²S audio codec for real signal in/out | ⏳ Planned |
| 5. Full EQ | Assemble the multi-band channel-strip EQ, tune, and test end-to-end | ⏳ Planned |

---

## Tech stack

- **Language:** Python 3 (prototyping) → C++ (target firmware)
- **Libraries:** `numpy`, `scipy.signal`, `matplotlib`
- **Target hardware:** Teensy 4.1 — NXP i.MX RT1062, ARM Cortex-M7 @ 600 MHz
- **Domain:** digital signal processing, audio engineering, embedded real-time systems

---

## Running the prototypes

```bash
python3 -m pip install numpy scipy matplotlib

cd "Learning Basics"
python3 SineWaveGenerator.py   # plots component sines and their sum
python3 scipy_basics.py        # prints continuous & discrete TFs and filter coefficients
```

---

## What this demonstrates

Control-systems theory from ETH Zürich's *Control Systems 1* applied beyond coursework:
filter theory derived by hand and cross-checked against `scipy.signal`; an explicit
continuous-to-discrete design path (Laplace `H(s)` → bilinear transform → difference
equation); and a deliberate prototype-then-port workflow that respects the constraints
(fixed sample rate, per-sample compute budget) of the embedded target it is built for.

---

## Motivation — no AI, on purpose

This is a deliberate **no-AI challenge**: all code and DSP derivations are written by
hand, the same way the work had to be done earlier (without AI assistance) during my
studies. It's not expected to be game-changing — the point is to actually internalise the
maths and embedded constraints by working them out myself rather than outsourcing the
thinking.

**In the interest of full transparency: this README is the only part of the project
produced with AI assistance.** Everything else — the filters, the derivations, the
Python — is my own work.

---

*Personal learning project — actively evolving.*
