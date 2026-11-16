# Scripts

| Script | Função |
| --- | --- |
| `generate_switch_plate.py` | Gera as placas de switches (14,0/14,1/14,2 mm), a tira de teste e as notas de impressão em `hardware/switch-plate/out/` |
| `generate_knob.py` | Gera, a partir do `Knob-X2` do Pehmis (intocado), o knob com o furo escolhido (Ø5,9 mm, `Knob-X2_plum15_bore-5.9mm.3mf`; outros tamanhos em `BORE_SIZES`) e a tira de teste de encaixe (Ø5,5 a 6,0) em `hardware/knob-plum/` |
| `generate_knob_steampunk.py` | Gera o knob steampunk (cabeça Ø15 serrilhada em diamante, topo liso) com o mesmo furo de `generate_knob.py` (Ø5,9 mm) em `hardware/knob-plum/`. O encaixe interno vem de `generate_knob.py` (importado, calculado em memória) e é conferido automaticamente |
| `parse_gerber.py` | Lê contorno e furos do Gerber do topo (`hardware/switch-plate/gerbers-top/gerber`); a variável `SOFLE_TOP_GERBER` sobrescreve a pasta |

## Uso (Python 3.12)

```sh
python -m venv .venv
.venv/Scripts/activate        # Windows (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt
python scripts/generate_switch_plate.py
```

O gerador não cria `preview.png`; esse arquivo é uma imagem ilustrativa. Para outra versão do Gerber, extraia `v2-gerber-top.zip` em `hardware/switch-plate/gerbers-top/`.
