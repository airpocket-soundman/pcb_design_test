# M5BasicBaseLite-Compatible

M5Stack Core向けのPort A/B/C/D/E拡張ベースボードを、EasyEDAで再構築するプロジェクトです。

## Design goals

- 50 mm x 50 mm、M5Stack CoreのM-Bus互換形状
- Grove互換 Port A x2、Port B/C/D/E
- JLCPCB PCBA向けのGerber、BOM、CPLを生成可能にする
- SK6812 x10およびLiPo端子は初版ではDNPオプションとする

## Upstream reference

This design is based on `akita11/M5BasicBaseLite`, distributed under the MIT License:

- https://github.com/akita11/M5BasicBaseLite
- Original author: Junichi Akita

See [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md).

## Status

The EasyEDA project is routed and the current manufacturing package has been exported to `fabrication/`.

- `EasyEDA/M5BasicBaseLite-Compatible.eprj2`: editable EasyEDA project
- `fabrication/M5BasicBaseLite-Compatible-Gerber.zip`: PCB fabrication data
- `fabrication/M5BasicBaseLite-Compatible-BOM.csv`: assembly BOM
- `fabrication/M5BasicBaseLite-Compatible-CPL.csv`: component placement data
- `fabrication/M5BasicBaseLite-Compatible.dsn` / `.ses`: external-router interchange and result

The routing result contains 117 traces and 3 vias, with no different-net same-layer crossings in the post-import geometry check. Before placing a paid PCBA order, complete the release gates in `docs/design-spec.md`, especially physical M-Bus stack-height fit and EasyEDA's interactive DRC report review.
