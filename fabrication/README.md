# Fabrication package

Generated from `EasyEDA/M5BasicBaseLite-Compatible.eprj2` on 2026-07-22.

| File | Purpose |
|---|---|
| `M5BasicBaseLite-Compatible-Gerber.zip` | PCB fabrication layers and drill files |
| `M5BasicBaseLite-Compatible-BOM.csv` | PCBA bill of materials (tab-separated CSV) |
| `M5BasicBaseLite-Compatible-CPL.csv` | Pick-and-place/component position list |
| `M5BasicBaseLite-Compatible.dsn` | EasyEDA routing input exported before routing |
| `M5BasicBaseLite-Compatible.ses` | Freerouting 2.2.4 result imported into EasyEDA |

The six Grove connectors contain through-hole electrical pins and are marked non-SMD in the CPL. Confirm through-hole assembly support or plan to hand-solder them. Do not order until the release gates in `../docs/design-spec.md` have been reviewed.
