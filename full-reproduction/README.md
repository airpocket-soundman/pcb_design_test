# M5BasicBaseLite full reproduction

This directory contains the complete EasyEDA reproduction imported from the upstream MIT-licensed KiCad project.

## Files

| File | Purpose |
|---|---|
| `M5BasicBaseLite-Full.eprj2` | Editable EasyEDA project containing schematic and PCB |
| `M5BasicBaseLite-Full-Gerber.zip` | Gerber and drill package exported by EasyEDA |
| `M5BasicBaseLite-Full-BOM.csv` | BOM exported by EasyEDA |
| `M5BasicBaseLite-Full-CPL.csv` | Placement data exported by EasyEDA |
| `upstream-drc-report.txt` | KiCad 9 DRC report for the unmodified upstream PCB source |

## Reproduction audit

- 68 PCB components (matches upstream 68 footprints)
- 495 copper traces (matches upstream 495 segments)
- 42 vias (matches upstream 42 vias)
- 2 copper pours (matches upstream 2 zones)
- 10 SK6812 side-emitting LEDs, U1 through U10
- LiPo/battery connectors and solder jumpers
- Top-side 2 x 15 M5Bus SMD pin header, CN7
- Bottom-side 2 x 15 M5Bus SMD pin socket, CN8
- Both M5Bus connectors contain 30 pads on a 2.54 mm contact grid and occupy the same board position with the required top/bottom mirroring

## DRC status

The imported design intentionally preserves the upstream geometry and net assignments. KiCad 9 reports 220 violations on the unmodified upstream board but zero unrouted items. Many violations are legacy-library, silkscreen, solder-mask, and footprint metadata warnings; 17 are `shorting_items`, primarily caused by the upstream bottom M5Bus socket using `unconnected-(CN8-Pad*)` net names on pads that are physically tied to the corresponding top M5Bus nets.

Therefore this directory is an exact reproduction/reference release, not yet a clean PCBA release. A manufacturing-clean derivative should normalize the CN7/CN8 net names, assign orderable supplier parts, then pass EasyEDA DRC without errors before ordering.
