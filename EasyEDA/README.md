# EasyEDA project files

- `M5BasicBaseLite-Compatible.eprj2` is the original local-project snapshot.
- `M5BasicBaseLite-Compatible-Final.epro2` is the final portable EasyEDA
  exchange project. Import/open this file in EasyEDA.
- `visual-final-patch.json` records the changes made by the browser
  visual-feedback pass.

Rebuild the portable final project from the reviewed production source with:

```powershell
python ..\tools\patch_epro2.py `
  ..\pcba\M5BasicBaseLite-PCBA-Production.epro2 `
  .\M5BasicBaseLite-Compatible-Final.epro2 `
  .\visual-final-patch.json
```

The final project preserves the JP2 5 V/3.3 V selector: CN3 pad 3 is routed to
JP2 pad 2 on `Net-(CN3-Pad3)`.
