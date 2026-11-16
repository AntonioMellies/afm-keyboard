# Contexto do projeto — Teclado Sofle v2

Responda em português do Brasil.

Repositório oficial de montagem de um teclado split **Sofle v2.0.1 (sem RGB)**, MX hot-swap, Pro Micro, QMK, case e placa de switches impressos. Veja o [README](README.md) para a estrutura.

## Regras

- `docs/` é só referência; nunca registre progresso ali. Progresso fica em `PROGRESS.md` local (copiado de `progress/PROGRESS.template.md`, ignorado pelo git). Itens novos de checklist vão no template.
- Nomes de pastas/arquivos em inglês; conteúdo em português.
- `hardware/case-pehmis/` é cópia de terceiros (CC BY-NC-SA 4.0, commit 1435ee8): não editar.
- A placa de switches é gerada por `scripts/generate_switch_plate.py` a partir do Gerber do topo; não edite os 3MF à mão.

## Decisões de projeto

- PCB na JLCPCB (parâmetros em `docs/04-pcb-order.md`). Topo e fundo impressos, não FR4.
- Pro Micro esquerdo com face limpa para cima, direito com componentes para cima; pontes dos 4 jumpers do OLED; botão de reset soldado por baixo da PCB.
- Pés de 8 mm em TPU; knob do Pehmis (`Knob-X2`, intocado) é adaptado ao eixo Plum 15 mm por `scripts/generate_knob.py`, que gera `hardware/knob-plum/`; só o furo do eixo muda. Furo escolhido no teste: Ø5,9 mm (o de 5,8 não entrou); só ele é gerado.
- Knob steampunk: `scripts/generate_knob_steampunk.py` importa `generate_knob.py`, gera o knob Plum de cada furo em memória e copia dele o encaixe interno (cavidade = cilindro Ø11 − knob de origem), conferindo por cortes. A haste Ø12,6 × 5,4 mm não pode crescer: entra no furo Ø14 do topo do case.
- Firmware: `firmware/build/sofle_rev1_afm.hex` (layout AFM ABNT2, alvo `sofle/rev1`), gravado com `qmk flash firmware/build/sofle_rev1_afm.hex`, uma metade por vez, sem TRRS.
- Todo firmware precisa de `#define SPLIT_USB_DETECT` (os Pro Micro clone alimentam VBUS pelo TRRS). Não use `.hex` do QMK Configurator nem o alvo `splitkb/aurora/sofle_v2` (pinagem diferente).
- Windows: o bootloader deve usar o driver serial da Microsoft; os pacotes da Arduino foram removidos com `pnputil`.
