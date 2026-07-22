# PCBA validation report

Date: 2026-07-22

Release decision: **NOT APPROVED FOR ORDER**

## Critical blocker: M5Bus bottom socket

The proposed low-profile socket Yxcon `F136-1215A0CMUB1` / LCSC `C41382298` is not footprint-compatible.

| Measurement | Existing J11 PCB footprint | C41382298 library land pattern |
|---|---:|---:|
| Contact pitch | 2.54 mm | 2.54 mm |
| SMD pad-row span | 5.04 mm | 5.82 mm |
| Difference | - | 0.78 mm total (0.39 mm per side) |

The 2.54 mm contact-row pitch does not imply identical SMD land spacing. The candidate would place its leads outside the existing pad centers. Its LCSC assignment has therefore been removed from J11 in the live EasyEDA project and from the connector BOM.

## M5Bus electrical validation

The upstream design intentionally keeps CN8/J11 pads 6, 7, 8, 9, 11, 13, 14, 24, 25, 27, and 29 on individual `unconnected-(CN8-Pad*)` nets. Pad 30 is `/BAT`, while the top header pad 30 is `Net-(J1-Pad1)`; these are joined through the bridged solder jumper JP1. These original assignments have been preserved in EasyEDA.

## EasyEDA DRC snapshot

| Category | Count | Assessment |
|---|---:|---|
| Clearance: Device to TH Pad | 35 | Imported J11 body/courtyard overlaps the intentional auxiliary through-hole pad array; requires footprint-rule cleanup before release |
| Physical: Via Diameter | 42 | Board uses 0.30 mm drills; imported EasyEDA rule incorrectly requires at least 0.50 mm |
| Netlist Error | 1 | Schematic and PCB netlists/designators are not synchronized after import and connector renaming |

There are no unrouted-connection errors in the current EasyEDA DRC snapshot. JLCPCB's published standard capability accepts a 0.15 mm via hole with 0.25 mm overall diameter for 2-layer boards, so the existing 0.30 mm drill is manufacturable; the EasyEDA rule must still be corrected and DRC rerun for a clean release.

## BOM/CPL audit

- The connector BOM is only a connector procurement table, not a complete PCBA BOM.
- Port A is assigned to red XUNPU `C22390444`.
- Port B and Ports C/D/E have requested hanxia manufacturer part numbers but no confirmed LCSC C-numbers.
- J10 is assigned to Kinghelm `C19630981`.
- J11 is unassigned and blocks assembly.
- The exported full BOM also lacks orderable LCSC assignments for the remaining LEDs, resistors, battery/header connectors, and other populated parts.
- CN1 remains DNP.

## Required release steps

1. Select a low-profile 2 x 15 M5Bus socket whose datasheet land pattern matches the 5.04 mm J11 SMD pad-row span, or redesign J11 to the selected socket and recheck mechanical clearance.
2. Confirm current LCSC C-numbers for the black and standard hanxia Grove connectors.
3. Complete the full assembly BOM and explicit DNP list.
4. Synchronize schematic/PCB designators and netlist.
5. Set the EasyEDA via rule to the chosen JLCPCB process capability and resolve or formally waive the intentional J11 body-to-TH-pad checks.
6. Rerun DRC, regenerate Gerber/BOM/CPL from the final EasyEDA revision, and inspect them in the JLCPCB quote interface before payment.
