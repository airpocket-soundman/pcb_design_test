# Design specification

## Board

- Overall envelope: 50 mm x 50 mm
- Outline: 18 straight segments matching the upstream KiCad Edge.Cuts, including 1 mm corner chamfers, the right-edge step, and the 4 mm x 3 mm bottom notch
- Mounting holes: 4 x 3.2 mm NPTH at (3,3), (47,3), (3,47), (47,47) mm
- Alignment holes: 4 x 2.1 mm NPTH at (7,3), (43,3), (6,47), (43,47) mm
- Target: M5Stack Core M-Bus compatible base
- EDA project: `M5BasicBaseLite-Compatible`

## Port mapping

| Port | Signal 1 | Signal 2 | Supply | Ground |
|---|---|---|---|---|
| A1 | IO22 | IO21 | +5V | GND |
| A2 | IO22 | IO21 | +5V | GND |
| B | IO36 | IO26 | +5V | GND |
| C | IO16 | IO17 | +5V | GND |
| D | IO34 | IO35 | +5V | GND |
| E | IO5 | IO13 | +5V | GND |

IO21 and IO22 use 4.7 kOhm pull-ups to +3.3V.

## PCBA parts

| Function | Candidate | LCSC part |
|---|---|---|
| Grove-compatible right-angle connector | WAFER-HY2.0-4PWZ-H62 | C22390454 |
| M-Bus 2x15 SMD male header | KH-2.54PH-2X15P-L11.0-SMT | C19630981 |
| 4.7 kOhm 0603 resistor | 0603WAF4701T5E | 0603WAF4701T5E.1 |

The Grove ports use four plated through-hole signal/power pins at 2.0 mm pitch plus two mechanical hold-down pads. The selected EasyEDA/LCSC device is `WAFER-HY2.0-4PWZ-H62` / `C22390454`. Because the electrical pins are through-hole, confirm the assembler's through-hole insertion/soldering option; they are intentionally marked non-SMD in the CPL.

The M5Bus connector contact grid is 2 x 15 with 2.54 mm pitch in both axes. This build uses only the top-side SMD male header; the opposite-side female socket is DNP. J7 is `KH-2.54PH-2X15P-L11.0-SMT` / LCSC `C19630981`, placed at (6 mm, 25 mm), top side, rotation 270 degrees, with pin 1 at the lower-left solder-pad row. It has 6 mm mating-pin length and 2.5 mm insulator height. Physical stack fit remains a release gate.

## Routing and manufacturing output

- External routing flow: EasyEDA DSN -> Freerouting 2.2.4 -> EasyEDA SES import
- Imported result: 117 copper traces, 3 vias, 13 routed nets
- Post-import geometry test: no different-net intersections on the same copper layer
- Gerber package includes top/bottom copper, silkscreen, solder mask, paste mask, board outline, PTH, NPTH, and via drill files
- BOM and CPL were exported directly from EasyEDA after routing

## Release gates before ordering

- Run EasyEDA's interactive DRC and review every remaining item. The API-triggered DRC in EasyEDA 3.2.149 does not return before the bridge's 30-second timeout, so an automated pass/fail result was not recorded.
- Confirm J7 pin-1 orientation and mating height against the exact M5Stack Core unit.
- Confirm that the PCBA vendor will assemble the six through-hole Grove connectors, or plan them as hand-soldered/DNP parts.
- Review the BOM substitutions and availability at order time.

## DNP options for the first build

- SK6812 side-emitting RGB LEDs x10
- LiPo connector and battery-selection jumpers
