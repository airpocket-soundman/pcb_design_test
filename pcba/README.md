# PCBA connector release

This directory contains the connector-focused PCBA package derived from the exact upstream reproduction.

## Port mapping

| Port | PCB designators | Required color | LCSC assignment |
|---|---|---|---|
| A | CN2, CN3 | Red | C22390444 / XUNPU WAFER-HY2.0-4PWZ-R62 |
| B | CN4 | Black | hanxia HX-HY2.0-4PWZ-B; obtain the current JLCPCB/LCSC C-number at quotation |
| C | CN5 | Beige / standard | hanxia HX-HY2.0-4PWZ |
| D | CN6 | Beige / standard | hanxia HX-HY2.0-4PWZ |
| E | CN7 | Beige / standard | hanxia HX-HY2.0-4PWZ |

CN1 is the optional vertical Grove connector in the upstream design and is DNP in this release.

## M5Bus

| Side | Designator | LCSC | Part |
|---|---|---|---|
| Top header | J10 | C19630981 | Kinghelm KH-2.54PH-2X15P-L11.0-SMT |
| Bottom low-profile socket | J11 | Unassigned | BLOCKED: compatible low-profile 2 x 15 socket not yet selected |

Both positions are 2 x 15 and use a 2.54 mm contact grid. The routed SMD land rows are approximately 5.04 mm apart because the surface-mount leads extend outward. The designators were changed from duplicated upstream identifiers to unique J10/J11 identifiers for assembly data.

The original 8.5 mm-high HCTL socket was rejected as too tall. The 3.55 mm-high Yxcon F136-1215A0CMUB1 (`C41382298`) was also rejected after land-pattern validation: its recommended SMD pad rows are 5.82 mm apart, while this PCB's rows are approximately 5.04 mm apart. J11 is deliberately left without an LCSC assignment until a mechanically compatible low-profile socket is found or the footprint is redesigned.

## Files

- `M5BasicBaseLite-PCBA-Gerber.zip`: review-only fabrication data from the full reproduction; **do not order it yet**.
- `M5BasicBaseLite-PCBA-CPL.csv`: placement data; the M5Bus references are normalized to J10/J11.
- `M5BasicBaseLite-PCBA-Connector-BOM.csv`: procurement and assembly table for all requested connectors.

## Ordering gates

- **DO NOT ORDER:** J11 has no validated low-profile socket and the package has not passed release DRC/BOM/CPL review.
- This connector BOM is not a complete assembly BOM. The resistors, LEDs, battery connectors, jumpers, and other populated items still require LCSC assignments or explicit DNP decisions.
- The Grove electrical pins are through-hole. Select mixed SMT/THT assembly and confirm wave/manual insertion support.
- Port B is specified by the exact hanxia MPN `HX-HY2.0-4PWZ-B`; the current JLCPCB/LCSC C-number must be selected during component matching.
- Ports C, D, and E use the standard-color hanxia `HX-HY2.0-4PWZ`; select its current JLCPCB/LCSC C-number during component matching.
- See `VALIDATION.md` for the measured footprint comparison, current EasyEDA DRC results, and release blockers.
