# PCBA validation report

Date: 2026-07-22

Release decision: **APPROVED FOR JLCPCB QUOTATION — HEADER-ONLY REVISION**

## Critical blocker: M5Bus bottom socket

The proposed low-profile socket Yxcon `F136-1215A0CMUB1` / LCSC `C41382298` is not footprint-compatible.

| Measurement | Existing J11 PCB footprint | C41382298 library land pattern |
|---|---:|---:|
| Contact pitch | 2.54 mm | 2.54 mm |
| SMD pad-row span | 5.04 mm | 5.82 mm |
| Difference | - | 0.78 mm total (0.39 mm per side) |

The 2.54 mm contact-row pitch does not imply identical SMD land spacing. The candidate would place its leads outside the existing pad centers. Its LCSC assignment was removed. For this approved header-only revision, J11 is removed from the PCB and assembly data.

## M5Bus electrical validation and header-only conversion

The upstream design intentionally kept CN8/J11 pads 6, 7, 8, 9, 11, 13, 14, 24, 25, 27, and 29 on individual `unconnected-(CN8-Pad*)` nets. Pad 30 was `/BAT`, while the top header pad 30 is `Net-(J1-Pad1)` and reaches `/BAT` through the bridged solder jumper JP1.

Removing J11 disconnected six even-numbered top-header signals from their existing bottom-layer traces. New bottom-layer bridges connect those trace ends directly to the plated auxiliary pads for `+3V3`, `/IO22`, `/IO17`, `/IO13`, `/IO5`, and `/IO26`. EasyEDA reports no remaining connection errors.

## EasyEDA DRC snapshot

| Category | Count | Assessment |
|---|---:|---|
| Copper/clearance errors | 0 | Pass |
| Physical/via errors | 0 | Pass after applying JLCPCB-capable 0.15 mm minimum drill and 0.25 mm minimum via diameter rules |
| Connection/unrouted errors | 0 | Pass |
| Netlist comparison | 1 | Accepted import limitation: the upstream schematic has no separate top M5Bus header symbol, while the PCB contains J10 |

JLCPCB's published standard capability accepts a 0.15 mm via hole with 0.25 mm overall diameter for 2-layer boards, so the existing 0.30 mm drill is within capability. The remaining netlist comparison is not a copper-connectivity error and is documented as a waiver for this imported OSHW design.

## BOM/CPL audit

- `M5BasicBaseLite-PCBA-Production-BOM.csv` is the complete populated-item BOM for this revision.
- Port A is assigned to red XUNPU `C22390444`.
- Port B and Ports C/D/E retain the requested exact hanxia MPNs and require JLCPCB global/custom sourcing.
- J10 is assigned to Kinghelm `C19630981`.
- R1/R2 are assigned to `C23162`; U1-U10 are assigned to `C5378721`.
- CN1, J1, J2, J3, and J11 are DNP. JP1/JP2 are fabricated copper features, not placed parts.
- The production CPL was filtered to the same 19 populated references represented by the BOM.

## Gerber audit

- The board outline is one closed 50 mm x 50 mm contour.
- Top/bottom copper, solder mask, paste, silkscreen, PTH, NPTH, and via drill files are present.
- SHA-256 checksums:
  - BOM: `689F1E983687CD98736300FC82E8E1AE67A866917EDD119329ADA2E20F3B52B3`
  - CPL: `25BB9C60BA64853C89666CC276965948F092042EE8E957BDE37C836E1CA3BC4B`
  - Gerber: `261CF83C9306B3E57789B357A3F01151C3FFC169DB65E026B4348AB59DA53FF7`
  - EasyEDA source: `95CB093CBBCAFC30EE372FB8F77105703DC6D87B8EE1DCB32C8581F066E6EC7E`

## Quotation-stage checks

1. Upload the three manufacturing files (`Gerber`, `BOM`, and `CPL`) with `Production` in their names. The `.epro2` file is the editable source and is not uploaded to the order form.
2. Select double-sided SMT plus through-hole assembly; all populated SMT parts are top-side except R1/R2 on the bottom.
3. Manually map the exact hanxia Grove MPNs and request custom sourcing where no C-number is offered.
4. Verify the interactive Gerber preview shows the closed 50 mm square outline and all holes.
5. Verify the placement preview has 19 references and no J11.
6. Do not pay if JLCPCB substitutes Grove colors/orientation or reports a footprint mismatch; return to the EasyEDA project for correction.
