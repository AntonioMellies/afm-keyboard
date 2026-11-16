# Lista de materiais (BOM)


> Parte da documentação de referência do projeto. Para marcar o que já foi feito, use `PROGRESS.md` (veja o [README](../README.md)).

Para as duas metades do Sofle v2 padrão (sem RGB), conforme o [guia oficial](https://josefadamcik.github.io/SofleKeyboard/build_guide.html) e a [página de compra de peças](https://josefadamcik.github.io/SofleKeyboard/sourcing_parts.html):

| Item | Qtd. (com reserva) | Especificação detalhada | AliExpress |
| --- | --- | --- | --- |
| PCB Sofle v2 | 2 | Mesma placa para os dois lados (reversível). Fabricação própria: Gerbers do GitHub, 2 camadas, FR4 1,6 mm, acabamento lead-free HASL ou ENIG. Confira se é v2 (sem RGB) e não v2.1 RGB | [Buscar kit PCB Sofle v2](https://www.aliexpress.com/w/wholesale-sofle-v2-pcb.html) |
| Placas de topo e fundo | 2 + 2 | FR4 (mesmo material da PCB), acrílico 3 mm ou alumínio. Arquivos de corte no repositório; muitos kits já incluem | [Buscar case sanduíche Sofle](https://www.aliexpress.com/w/wholesale-sofle-v2-case-plate.html) |
| Sockets hot-swap Kailh MX | 58 (+5) | Modelo Kailh CPG151101S11 para MX (não confundir com o socket Choc). Vendidos em pacotes de 10–100 | [Produto da lista oficial](https://www.aliexpress.com/item/32951252318.html) · [Buscar](https://www.aliexpress.com/w/wholesale-kailh-mx-hotswap-socket.html) |
| Diodos 1N4148W | 58 (+10) | SMD, encapsulamento SOD-123 (não SOD-323 nem MiniMELF), código de marcação "T4". Rolos de 100 custam pouco | [Produto da lista oficial](https://www.aliexpress.com/item/32334222067.html) · [Buscar](https://www.aliexpress.com/w/wholesale-1n4148w-sod123.html) |
| Switches MX | 58 (+2) | Qualquer switch compatível com MX, 3 ou 5 pinos. Se a placa não tiver furos para os pinos plásticos laterais, corte-os. Lineares (Red, Yellow), táteis (Brown) ou clicky (Blue) | [Buscar switches MX](https://www.aliexpress.com/w/wholesale-gateron-mx-switch.html) |
| Keycaps | 58 | Prefira perfil uniforme (DSA, XDA, SA uniforme): no layout em colunas, perfis esculpidos (Cherry, OEM) ficam com alturas trocadas. Inclua duas 1.5u para os polegares, ou use só 1u | [Buscar keycaps DSA/XDA em branco](https://www.aliexpress.com/w/wholesale-xda-blank-keycaps.html) |
| Microcontrolador Pro Micro | 2 | ATmega32U4, versão 5 V / 16 MHz (evite 3,3 V / 8 MHz). Há versões micro-USB e USB-C; evite Arduino Micro ou Mini | [Produto da lista oficial](https://www.aliexpress.com/item/32849563958.html) · [Buscar Pro Micro USB-C](https://www.aliexpress.com/w/wholesale-pro-micro-atmega32u4-type-c.html) |
| Alternativa: RP2040 Pro Micro | 2 | Mesma pinagem do Pro Micro, USB-C, 4–16 MB de flash; usa o conversor do QMK (`CONVERT_TO=promicro_rp2040`). Recomendado para iniciantes | [Buscar RP2040 Pro Micro](https://www.aliexpress.com/w/wholesale-rp2040-pro-micro-type-c.html) |
| Headers/sockets para o MCU | 4 × 12 pinos | Opção removível: pinos redondos de baixo perfil, fêmea na PCB e macho no MCU. Opção fixa: barras macho que vêm com o Pro Micro | [Fêmea redondo (lista oficial)](https://www.aliexpress.com/item/32817226478.html) · [Macho redondo (lista oficial)](https://www.aliexpress.com/item/32803164240.html) |
| Jack TRRS PJ-320A | 2 (+1) | Fêmea 3,5 mm, 4 polos, 4 pinos; o mesmo do Corne e Lily58. Não use PJ-320D (pinagem diferente) | [Produto da lista oficial](https://www.aliexpress.com/item/32869968774.html) · [Buscar](https://www.aliexpress.com/w/wholesale-pj-320a-trrs.html) |
| Cabo TRRS | 1 | Macho-macho 3,5 mm de 4 polos (P2 com microfone). Comprimento de 30–100 cm; cabos espiralados ou com plug em 90° liberam espaço entre as metades | [Buscar cabo TRRS](https://www.aliexpress.com/w/wholesale-trrs-cable-3.5mm-4-pole-male.html) |
| Botão tátil de reset | 2 (+2) | THT de 2 pinos, 6 × 3,5 mm (ex.: 6×3,5×4,3 mm) | [Produto da lista oficial](https://www.aliexpress.com/item/32981768203.html) · [Buscar](https://www.aliexpress.com/w/wholesale-tactile-switch-6x3.5-2-pin.html) |
| Display OLED | 2 | 0,91", 128×32, controlador SSD1306, interface I²C de 4 pinos. Confira se a ordem dos pinos (GND, VCC, SCL, SDA) bate com a serigrafia da PCB | [Produto da lista oficial](https://www.aliexpress.com/item/32712441521.html) · [Buscar](https://www.aliexpress.com/w/wholesale-oled-0.91-128x32-ssd1306-i2c.html) |
| Headers para OLED | 2 × 4 pinos | Barra fêmea 1×4 na PCB, com altura que deixe o OLED acima do MCU com sockets | [Buscar barra fêmea 2,54 mm](https://www.aliexpress.com/w/wholesale-female-pin-header-2.54mm-1x4.html) |
| Encoder rotativo EC11E | 2 | EC11 com botão (push), 20 detents, eixo de 15–20 mm. Evite EC11K (pinos plásticos sem furo na PCB) | [Produto da lista oficial](https://www.aliexpress.com/item/4000891003225.html) · [Buscar](https://www.aliexpress.com/w/wholesale-ec11-rotary-encoder.html) |
| Knob para encoder | 2 | Compatível com o eixo do encoder (serrilhado ou em D, 6 mm); alumínio fica mais bonito | [Produto da lista oficial](https://www.aliexpress.com/item/2028814958.html) · [Buscar](https://www.aliexpress.com/w/wholesale-aluminum-knob-6mm-encoder.html) |
| Espaçadores M2 | 10 (+4) | Latão ou alumínio, fêmea-fêmea, 6–8 mm para MX (8 mm é o comum em cases FR4). +4 para a tampa do OLED | [Kit de espaçadores M2 (lista oficial)](https://www.aliexpress.com/item/32974970926.html) · [Buscar](https://www.aliexpress.com/w/wholesale-m2-brass-standoff-kit.html) |
| Parafusos M2 | 20 (+8) | M2 × 4 mm, cabeça Phillips ou Allen; precisam caber dois por espaçador | [Buscar parafusos M2x4](https://www.aliexpress.com/w/wholesale-m2x4-screw.html) |
| Pés de borracha | 8–10 | Adesivos, \~10 mm de diâmetro | [Produto da lista oficial](https://www.aliexpress.com/item/32839661456.html) · [Buscar](https://www.aliexpress.com/w/wholesale-adhesive-rubber-feet-10mm.html) |
| Cabo USB | 1 | Micro-USB ou USB-C, conforme o MCU; precisa transmitir dados (não serve cabo só de carga) | — |
| Tampa de acrílico para OLED | 2 | Opcional; a v2 não tem arquivo oficial de tampa | — |

Dica: com exceção dos encoders e knobs, as peças são as mesmas do Lily58, então kits de peças do Lily58 servem.

**Sobre os links:** "Produto da lista oficial" são os anúncios usados e indicados pelo criador do Sofle na [página de compra de peças](https://josefadamcik.github.io/SofleKeyboard/sourcing_parts.html). Eles foram publicados há alguns anos e podem estar indisponíveis ou exigir login. "Buscar" abre uma busca no AliExpress com os termos certos. Antes de comprar, confira a especificação do anúncio com a tabela acima.

**Dicas de compra:**

- Compre peças a mais de diodos, sockets e botões. Elas são baratas, pequenas e fáceis de perder ou queimar.
- Kits de PCB costumam incluir diodos, sockets, jacks, botões e espaçadores. Compare o que vem no kit com a tabela antes de comprar avulso.
- Prefira vendedores com muitas avaliações e fotos reais. Para MCU e OLED, compre de uma loja que aceite troca por defeito.

## Materiais extras do case impresso

| Item | Qtd. | Observação |
| --- | --- | --- |
| Espaçadores M2 × 8 mm | 10 | Já listados acima |
| Parafusos M2 × 4 mm (placa e PCB no fundo) | 20 | Kit de parafusos M2 |
| Parafusos M2 × 8 mm (fecham o case) | 10 | Kit de parafusos M2 |
| Insertos roscados M2 × 4 × 3,5 mm (*heat-set*) | 10 | Instalados nas peças `L-Top` e `R-Top` |
| Ímãs de neodímio 8 × 3 mm | 8 | Só se usar os apoios de pulso |
| Pés de 8 mm | 16 | Impressos em TPU (os encaixes do case são de 8 mm) |
| Cola instantânea (cianoacrilato) ou epóxi | — | Para fixar os ímãs |

## Itens impressos em 3D

- **Placa de switches (2):** gerada neste repositório, veja [3D](05-3d-printing.md).
- **Case Pehmis:** `L/R-Top`, `L/R-Bottom`, `L/R-Wristrest` (opcional) e `Knob-X2`.
- **Pés em TPU e knobs:** veja [3D](05-3d-printing.md).

## Onde comprar no Brasil e dicas

Kits completos são raros no varejo nacional; o caminho mais comum é comprar PCB e peças importadas e completar com eletrônicos genéricos locais.

- **Kit completo importado:** AliExpress e lojas como beekeeb, KeebMaker, Mechboards ou splitkb vendem kits Sofle v2/RGB, com ou sem solda prévia. Confira se o kit é v2, v2.1 RGB ou fork (Keyhive), pois o firmware muda.
- **PCB sob encomenda:** envie os Gerbers do GitHub a um fabricante como JLCPCB ou PCBWay (2 camadas, 1,6 mm). O pedido mínimo costuma ser 5 placas — dá para dividir com amigos.
- **Eletrônicos genéricos:** Pro Micro, OLED SSD1306, encoder EC11, jack PJ-320A, botões táteis e diodos 1N4148W são encontrados no Mercado Livre e em lojas de eletrônica/Arduino nacionais, geralmente com entrega mais rápida.
- **Switches e keycaps:** comunidades e lojas de teclados mecânicos nacionais vendem switches MX e keycaps; confirme que os keycaps tenham duas 1.5u ou use só 1u.
- **Impostos:** compras internacionais pagam imposto de importação e ICMS; verifique as regras vigentes antes de dividir ou juntar pedidos.
- **Dica de primeira montagem:** prefira um MCU RP2040 compatível com Pro Micro (USB-C, menos frágil) e use sockets — facilita trocar o controlador se algo der errado.
