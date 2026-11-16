# Progresso da montagem

> **Como usar:** copie este arquivo para `PROGRESS.md` na raiz (ignorado pelo git) e marque `[x]` conforme avança. Para uma nova montagem, copie de novo. Este arquivo é só um checklist; as instruções ficam em [`docs/`](../docs/).

- Início: ____/____/______
- Observações / variações desta montagem:

## 1. Compras ([BOM](../docs/02-bom.md))

- [ ] 2× Pro Micro ATmega32U4 5 V/16 MHz (USB-C)
- [ ] Sockets Kailh MX hot-swap (≥ 58 + reserva)
- [ ] Diodos 1N4148W SOD-123 (≥ 58 + reserva)
- [ ] Switches MX (≥ 58 + reserva)
- [ ] Keycaps de perfil uniforme (duas 1.5u ou só 1u)
- [ ] 2× OLED 0,91" SSD1306 + barras fêmea de 4 pinos
- [ ] 2× encoder EC11 (eixo Plum 15 mm)
- [ ] Jacks PJ320A + cabo TRRS
- [ ] Botões táteis 6×6×4,3 mm
- [ ] Espaçadores M2 × 8 mm (10 + reserva) e kit de parafusos M2/M2,5/M3
- [ ] Insertos roscados M2 × 4 × 3,5 mm (10)
- [ ] Ímãs 8 × 3 mm (8; só com apoios de pulso)
- [ ] Opcional: barras fêmea 1×12 para socket do Pro Micro
- [ ] Cabo USB-C (dados) e [ferramentas](../docs/03-tools.md)

## 2. PCB ([pedido](../docs/04-pcb-order.md))

- [ ] Pedido feito (parâmetros do documento)
- [ ] PCBs recebidas e conferidas

## 3. Impressão 3D ([guia](../docs/05-3d-printing.md))

- [ ] Tira de teste de tolerância impressa; furo escolhido: ______ mm
- [ ] 2× placa de switches
- [ ] L-Top
- [ ] R-Top
- [ ] L-Bottom
- [ ] R-Bottom
- [ ] Tira de teste de encaixe do eixo Plum (`hardware/knob-plum/`)
- [ ] 2× Knob Plum 15 mm (Knob-X2 adaptado ou steampunk)
- [ ] Pés de 8 mm em TPU
- [ ] Opcional: L-Wristrest / R-Wristrest

## 4. Montagem ([passo a passo](../docs/06-assembly.md))

- [ ] Diodos
- [ ] Sockets hot-swap
- [ ] Botão de reset (por baixo da PCB) e jack TRRS
- [ ] Pontes dos 4 jumpers do OLED
- [ ] Pro Micro (esquerdo: face limpa para cima; direito: componentes para cima)
- [ ] OLEDs e encoders
- [ ] Teste de todas as teclas antes de fechar

## 5. Firmware ([guia](../docs/07-firmware.md))

- [ ] Ambiente QMK instalado
- [ ] Bootloader aparece como "Dispositivo Serial USB" (Microsoft) no Gerenciador de Dispositivos
- [ ] Metade esquerda gravada
- [ ] Metade direita gravada
- [ ] TRRS conectado e split funcionando

## 6. Fechamento

- [ ] Insertos roscados nos Tops
- [ ] Placa + PCB aparafusadas nos Bottoms
- [ ] Case fechado, knobs, pés (e ímãs, se aplicável)
- [ ] Keycaps
- [ ] Teclado em uso
