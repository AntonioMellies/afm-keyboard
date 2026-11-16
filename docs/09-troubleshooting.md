# Solução de problemas

> Parte da documentação de referência do projeto. Para marcar o que já foi feito, use `PROGRESS.md` (veja o [README](../README.md)).

A maioria das falhas vem de solda fria, diodo invertido ou MCU na orientação errada — teste antes de fechar o case.

| Sintoma | Causa provável | O que fazer |
| --- | --- | --- |
| Nada acende ao ligar o USB, ou o Pro Micro esquenta | Curto entre VCC e GND ou entre trilhas vizinhas (ponte de solda) | Desconecte na hora; com o multímetro em continuidade, procure o curto antes de ligar de novo |
| Uma tecla não funciona | Solda fria no socket ou no diodo; diodo invertido | Refaça a solda; confira a listra do diodo contra a serigrafia; teste o socket com pinça |
| Uma linha ou coluna inteira falha | Pino do MCU mal soldado ou socket com mau contato | Refaça a solda do pino correspondente; teste continuidade com multímetro |
| Metade direita não responde | Cabo TRRS solto/defeituoso, jack mal soldado ou firmware diferente nas metades | Grave o mesmo firmware nas duas; troque o cabo; revise o jack |
| A metade sem USB nunca funciona, de nenhum lado, mas o LED do Pro Micro acende pelo TRRS | Pro Micro clone alimenta o pino VBUS pelo TRRS; as duas metades se acham ligadas ao USB | Grave um firmware com `#define SPLIT_USB_DETECT` (`firmware/build/`) |
| Uma metade ligada sozinha digita espelhado | Normal: sem lateralidade definida, a metade no USB é sempre a esquerda | Use o USB na esquerda com o TRRS ligado |
| Toolbox: `ser_send(): write error` / `programmer is not responding` | Driver antigo da Arduino (2015) no bootloader | Remova os pacotes da Arduino com `pnputil` até a porta aparecer como "Dispositivo Serial USB" (Microsoft) |
| Toolbox: `connected ... []` seguido de "Flash complete" sem saída do avrdude | O Toolbox viu o bootloader antes de o Windows criar a porta COM | Nada foi gravado; repita, ou use `qmk flash` no QMK MSYS |
| Toolbox: `can't open device COMxx` ou assinatura `0xffffff` | O bootloader saiu antes ou durante a gravação (janela de <1 s com um toque só) | Reset duplo rápido; afaste a pinça de RST-GND logo depois |
| Lado esquerdo e direito trocados | Lateralidade definida pelo USB | Ligue o USB à esquerda ou grave com `-bl avrdude-split-left/right` |
| OLED não liga | Pontes de jumper do OLED não feitas; display ao contrário | Faça as 4 pontes; confira a ordem GND/VCC/SCL/SDA |
| Atraso na digitação sem OLED em um lado | Faltam pull-ups no I²C | Solde resistores de 4,7 kΩ em R1/R2 ou desative o OLED no firmware |
| Encoder gira ao contrário | Pinos A/B invertidos no firmware | Inverta a direção na keymap ou no VIA/Vial |
| Elite-C v3.0 instável no split | Bug da revisão 3.0 | Adicione `#define SPLIT_USB_DETECT` ao `config.h` (corrigido na v3.1) |
| Teclado reinicia ou trava ao mexer no cabo | TRRS conectado com USB ligado | Sempre desconecte o USB antes de mexer no TRRS |

Se o MCU for soldado direto e estiver com defeito, a troca é difícil — mais um motivo para usar sockets.

---

← [Switches e keycaps](08-switches-keycaps.md) · [Índice](../README.md#documentação) · [Referências e fontes](10-references.md) →
