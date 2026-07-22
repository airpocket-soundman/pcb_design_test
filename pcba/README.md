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
| Bottom low-profile socket | J11 | C41382298 | Yxcon F136-1215A0CMUB1, 3.55 mm insulation height |

Both are 2 x 15, 2.54 mm pitch, 2.54 mm row spacing, vertical surface-mount parts. The designators were changed from duplicated upstream identifiers to unique J10/J11 identifiers for assembly data.

The original 8.5 mm-high HCTL socket was rejected as too tall. J11 now uses the 3.55 mm-high Yxcon low-profile socket. The routed upstream pad geometry is retained; compare it with the Yxcon recommended land pattern before releasing the order.

## Files

- `M5BasicBaseLite-PCBA-Gerber.zip`: unchanged routed copper and board fabrication data from the full reproduction.
- `M5BasicBaseLite-PCBA-CPL.csv`: placement data; the M5Bus references are normalized to J10/J11.
- `M5BasicBaseLite-PCBA-Connector-BOM.csv`: procurement and assembly table for all requested connectors.

## Ordering gates

- The Grove electrical pins are through-hole. Select mixed SMT/THT assembly and confirm wave/manual insertion support.
- Port B is specified by the exact hanxia MPN `HX-HY2.0-4PWZ-B`; the current JLCPCB/LCSC C-number must be selected during component matching.
- Ports C, D, and E use the standard-color hanxia `HX-HY2.0-4PWZ`; select its current JLCPCB/LCSC C-number during component matching.
- The exact-reproduction PCB still inherits upstream DRC issues described in `../full-reproduction/README.md`. Gerber is provided for review, not as an unconditional order approval, until those electrical DRC items are closed.
