# CS EQ Teensy 4.1 — Project Log

## Project Overview
Building a digital equalizer (SSL-style) targeting the Teensy 4.1 microcontroller.

---

## Current Phase: Learning Basics

### Goals
- Understand core signal processing concepts (sine waves, filtering)
- Prototype and validate filter designs in Python before porting to C++/Teensy

### Files
| File | Status | Description |
|------|--------|-------------|
| `Learning Basics/SineWaveGenerator.py` | Done | Generates and plots single + summed sine waves |
| `Learning Basics/Filtering_Basics_with_ScipySignal.py` | In progress | Filter design & application using scipy.signal |
| `Learning Basics/Ressources/` | Reference | scipy.signal manual (v1.17.0) |

---

## Log

### 2026-02-04
- Project log created
- Phase: Learning Basics
- `SineWaveGenerator.py` — basic sine wave generation and summing in place
- `Filtering_Basics_with_ScipySignal.py` — stub created, next step

---

## Upcoming Phases
1. **Filter Design** — Design EQ band filters (low shelf, high shelf, peaking) in Python, validate with plots
2. **Teensy Prototype** — Port validated filter coefficients to C++ on Teensy 4.1
3. **Audio I/O** — Wire up ADC/DAC or I2S codec on Teensy
4. **Full EQ** — Assemble multi-band EQ, tune and test end-to-end
