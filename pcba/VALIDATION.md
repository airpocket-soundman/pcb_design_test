# PCBA validation report

Date: 2026-07-22

Release decision: **APPROVED FOR JLCPCB QUOTATION — M5BUS SOCKET REVISION**

## M5Bus bottom socket redesign

The low-profile socket is Yxcon `F136-1215A0CMUB1` / LCSC `C41382298`.

| Measurement | Original imported J11 footprint | Production J11 / C41382298 |
|---|---:|---:|
| Contact pitch | 2.54 mm | 2.54 mm |
| SMD pad-row span | 5.04 mm | 5.82 mm |
| Difference | - | 0.78 mm total (0.39 mm per side) |

The 2.54 mm contact-row pitch does not imply identical SMD land spacing. Therefore the old J11 footprint was removed and replaced with the official C41382298 EasyEDA/LCSC device instead of reusing incompatible lands.

## M5Bus electrical validation

The production socket is connected by physical M5Bus position rather than blindly copying the candidate footprint's pad numbers. Bottom-side mirroring swaps the candidate's odd/even numbering relative to the imported footprint, so every J11 pad was matched to J10 by X/Y position and net.

All 30 J11 pads match the corresponding J10 physical-position nets. Thirty short bottom-layer routes connect J11 to the existing plated auxiliary pads. The final `Net-(J1-Pad1)` position uses a new 0.30 mm drilled via. The net name was normalized consistently across pads, tracks, and vias. EasyEDA reports no connection errors.

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
- J10 is assigned to Kinghelm `C19630981`; J11 is assigned to Yxcon `C41382298`.
- R1/R2 are assigned to `C23162`; U1-U10 are assigned to `C5378721`.
- CN1, J1, J2, and J3 are DNP. JP1/JP2 are fabricated copper features, not placed parts.
- The production CPL was filtered to the same 20 populated references represented by the BOM, including bottom-side J11 at 270 degrees.

## Gerber audit

- The board outline is one closed 50 mm x 50 mm contour.
- Top/bottom copper, solder mask, paste, silkscreen, PTH, NPTH, and via drill files are present.
- SHA-256 checksums:
  - BOM: `55E4B6D40A7525113BBEB2632646B71D4821855F717E1F96DAF2432732028EA9`
  - CPL: `D8301D119A64D7F5E9E9DFDF81F362FF28D2120F3F6104F8186E657AEB7DE3DE`
  - Gerber: `EF77F0EA85CCDD0B6211F3F548D4399409698C2814503029867084A93CA8F8CB`
  - EasyEDA source: `5B3E82DD87DC39659B3471DC288500BE9C49F34C4EBDD8483D7C9B6294C0575D`

## Quotation-stage checks

1. Upload the three manufacturing files (`Gerber`, `BOM`, and `CPL`) with `Production` in their names. The `.epro2` file is the editable source and is not uploaded to the order form.
2. Select double-sided SMT plus through-hole assembly; R1/R2 and J11 are bottom-side parts.
3. Manually map the exact hanxia Grove MPNs and request custom sourcing where no C-number is offered.
4. Verify the interactive Gerber preview shows the closed 50 mm square outline and all holes.
5. Verify the placement preview has 20 references and shows J11 on the bottom at 270 degrees.
6. Do not pay if JLCPCB substitutes Grove colors/orientation or reports a footprint mismatch; return to the EasyEDA project for correction.
