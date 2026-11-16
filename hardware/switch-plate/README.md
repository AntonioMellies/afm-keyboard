# Placa de switches

Placa de 1,5 mm derivada do Gerber oficial do topo v2.0.1 (`gerbers-top/`, extraído de `hardware/pcb/gerbers/v2-gerber-top.zip`).

- `out/switch-plate_14.0mm.3mf`, `_14.1mm.3mf`, `_14.2mm.3mf`: placa com furos de cada tamanho (furos M2 alargados para 2,4 mm)
- `out/tolerance-test_14.0-14.2mm.3mf`: tira de teste (1, 2 ou 3 marcadores = 14,0 / 14,1 / 14,2 mm)
- `out/print-settings_bambu_PLA.txt`: ajustes sugeridos
- `out/preview.png`: imagem ilustrativa

Regerar: `python scripts/generate_switch_plate.py` ([scripts/README.md](../../scripts/README.md)). Impressão: [docs/05-3d-printing.md](../../docs/05-3d-printing.md).
