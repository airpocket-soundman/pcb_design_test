# PCBA validation report

Date: 2026-07-24

Release decision: **APPROVED FOR JLCPCB QUOTATION — VISUALLY REVIEWED REVISION**

## Browser visual-feedback revision

The final PCB was loaded into `eda-vision-loop` after every material change and
reviewed as separate top- and bottom-layer views. The visual loop produced these
final corrections:

- Port labels A/B/C/D/E/A′ were aligned and rotated for normal reading.
- The optional vertical Grove position is marked `A ALT`.
- The 50 mm x 50 mm outline, side notches, mounting holes, Grove positions, and
  the aligned top/bottom M5Bus connectors were checked in the rendered view.
- CN3/A′ pad 3 was found to be physically unrouted. The initial direct-to-5 V
  repair was rejected after checking the schematic intent: JP2 must retain the
  5 V/3.3 V selector. The final bottom-layer track therefore connects CN3 pad 3
  to JP2 pad 2 on `Net-(CN3-Pad3)`.
- The final browser render contains 2,232 PCB records. Its sole viewer finding
  is that 42 `RULE_SELECTOR` records are not rendered; this is a viewer
  limitation and not a PCB DRC error.

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
| Netlist comparison | 1 | Accepted import limitation: the imported schematic uses one M5Bus symbol while the PCB deliberately contains separate J10 top-header and J11 bottom-socket assembly components |

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
  - Visually reviewed Gerber: `BAE207FCFB097C02A36448594D64AA6974EEEDA6E9F5C4883BEA29925068C540`
  - Final EasyEDA source: `C9A4E53F15BD5C3720110B3B7A42A7F2837A315FF043AB299F43463431A3B7FA`

## Quotation-stage checks

1. Upload `M5BasicBaseLite-PCBA-Visual-Final-Gerber.zip` plus the existing
   `M5BasicBaseLite-PCBA-Production-BOM.csv` and
   `M5BasicBaseLite-PCBA-Production-CPL.csv`. The `.epro2` file is the editable
   source and is not uploaded to the order form.
2. Select double-sided SMT plus through-hole assembly; R1/R2 and J11 are bottom-side parts.
3. Manually map the exact hanxia Grove MPNs and request custom sourcing where no C-number is offered.
4. Verify the interactive Gerber preview shows the closed 50 mm square outline and all holes.
5. Verify the placement preview has 20 references and shows J11 on the bottom at 270 degrees.
6. Do not pay if JLCPCB substitutes Grove colors/orientation or reports a footprint mismatch; return to the EasyEDA project for correction.
