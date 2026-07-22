# PCBA header-only production release

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
| Bottom low-profile socket | J11 | DNP | Removed in this header-only production revision |

Both positions are 2 x 15 and use a 2.54 mm contact grid. The routed SMD land rows are approximately 5.04 mm apart because the surface-mount leads extend outward. The designators were changed from duplicated upstream identifiers to unique J10/J11 identifiers for assembly data.

The original 8.5 mm-high HCTL socket was rejected as too tall. The 3.55 mm-high Yxcon F136-1215A0CMUB1 (`C41382298`) was also rejected after land-pattern validation: its recommended SMD pad rows are 5.82 mm apart, while this PCB's rows are approximately 5.04 mm apart. The user previously approved a pin-header-only build, so J11 is removed from this manufacturing revision. Six bottom-layer routes formerly completed through the J11 lands were extended directly to the auxiliary plated holes.

## Files

- `M5BasicBaseLite-PCBA-Production-Gerber.zip`: current header-only fabrication package.
- `M5BasicBaseLite-PCBA-Production-CPL.csv`: filtered placement file containing the 19 populated references only.
- `M5BasicBaseLite-PCBA-Production-BOM.csv`: complete production BOM exported from EasyEDA.
- `M5BasicBaseLite-PCBA-Production.epro2`: editable EasyEDA production project matching these outputs.
- `M5BasicBaseLite-PCBA-Connector-BOM.csv`: connector sourcing details and DNP decisions.
- Files without `Production` in their names are retained only as historical review artifacts.

## Ordering gates

- This revision is ready to upload for a JLCPCB/JLCPCB Assembly quotation as a header-only build.
- J1, J2, J3, CN1, J11, JP1, JP2, mounting-hole/logo helpers, and auxiliary pads are excluded from assembly. JP1 and JP2 remain as fabricated copper jumpers.
- R1/R2 use `C23162`; U1-U10 use `C5378721`; J10 uses `C19630981`; the two red Port A connectors use `C22390444`.
- The Grove electrical pins are through-hole. Select mixed SMT/THT assembly and confirm wave/manual insertion support.
- Port B is specified by the exact hanxia MPN `HX-HY2.0-4PWZ-B`; request JLCPCB global/custom sourcing during component matching.
- Ports C, D, and E use the exact standard-color hanxia `HX-HY2.0-4PWZ`; request JLCPCB global/custom sourcing during component matching.
- Do not accept an automatic substitute for the Grove connectors without checking color, orientation, and the 2.00 mm land pattern.
- See `VALIDATION.md` for the final DRC, Gerber, BOM, and CPL audit.
