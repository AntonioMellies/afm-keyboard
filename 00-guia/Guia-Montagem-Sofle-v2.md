# Guia de Montagem — Teclado Sofle v2

Oct 21, 2026 · @Antonio

## Visão geral

O Sofle v2 é um teclado split (dividido) de 58 teclas, com colunas escalonadas (6×4 + 5 teclas de polegar por lado), projetado por Josef Adamčík a partir do Lily58, Corne e Helix ([projeto no GitHub](https://github.com/josefadamcik/SofleKeyboard)). Cada metade tem um microcontrolador próprio e as duas se ligam por um cabo TRRS; o computador se conecta por USB à metade esquerda.

- **Teclas:** 58 no total (29 por lado), sendo 5 de polegar por lado.
- **Extras:** um display OLED 128×32 e um encoder rotativo (knob) por lado, ambos opcionais.
- **Switches:** a v2 aceita apenas switches MX, sempre em sockets hot-swap Kailh (sem soldar os switches).
- **Firmware:** QMK (com suporte a VIA/Vial); variantes sem fio usam ZMK.

**Diferença principal da v2 para a v1:** na v2 o Pro Micro da metade direita é montado com a face dos componentes para cima, enquanto na esquerda fica com a face limpa para cima; a v1 também aceitava Choc. As versões RGB, Choc e Pico têm guias próprios (ver Variações).

## Lista de materiais (BOM)

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

### Status das compras

Atualizado em 22/10/2026. Total gasto até agora: **cerca de R$ 520,52** (AliExpress R$ 434,44, Amazon R$ 23,50, Shopee R$ 62,58).

| Item | Situação | Onde | Observação |
| --- | --- | --- | --- |
| PCB Sofle v2 + placas de topo e fundo | ❌ **Falta** | — | Item principal; confirme que é v2 e não v2.1 RGB |
| Pro Micro ATmega32U4 5 V/16 MHz USB-C | ✅ Comprado (2) | AliExpress | Vem com pinos macho |
| Sockets Kailh MX "1511" | ✅ Comprado (70) | AliExpress | 12 de reserva |
| Diodos 1N4148W T4 SOD-123 | ✅ Comprado (100) | AliExpress | 42 de reserva |
| Switches MX táteis "Brown" (marca genérica) | ✅ Comprado (100) | Shopee | Haste em cruz MX; 42 de reserva. Teste alguns ao chegar: marcas genéricas variam de lote para lote |
| Keycaps XDAL, 96 teclas | ✅ Comprado (1 kit) | AliExpress | Perfil uniforme baixo (família XDA), haste MX. Confira se o kit tem duas 1.5u (Tab e \\) e marcação em F e J |
| OLED 0,91" SSD1306 | ✅ Comprado (2) | AliExpress | Confira a ordem dos pinos |
| Barra fêmea 4 pinos (OLED) | ✅ Comprado (10) | AliExpress |  |
| Encoder EC11, eixo Plum 15 mm | ✅ Comprado (2) | AliExpress | Sem reserva |
| Jack PJ320A | ✅ Comprado (10) | AliExpress |  |
| Cabo P3 3,5 mm (TRRS) 50 cm | ✅ Comprado (1) | Amazon |  |
| Botão tátil 6×6×4,3 mm | ✅ Comprado (20) | AliExpress |  |
| Espaçadores M2 × 8 mm | ✅ Comprado (20) | AliExpress |  |
| Parafusos M2 (kit Phillips) | ✅ Comprado (1 kit) | AliExpress | Use M2 de 4–5 mm |
| Knobs | 🖨️ Imprimir | — | Furo serrilhado de 6 mm |
| Pés | 🖨️ Imprimir | — | De preferência em TPU |
| Barra fêmea 1×12 (socket do MCU) | ⚪ Opcional | — | Só se quiser o Pro Micro removível |
| Cabo USB-C e ferramentas | ✅ Já tem | — |  |

## Ferramentas

Um ferro de solda com controle de temperatura e uma pinça fina resolvem quase toda a montagem; o resto é apoio.

- **Essenciais:** ferro de solda (ideal com temperatura ajustável, ponta fina ou chanfrada), solda fina (0,5–0,8 mm, com fluxo), pinça de precisão, óculos de proteção, fita crepe, chave de fenda/Phillips pequena.
- **Recomendados:** extrator de fumaça, lupa ou lente de aumento, boa iluminação, fluxo extra, malha dessoldadora, multímetro (teste de continuidade), álcool isopropílico e cotonetes para limpar o fluxo.

## Passo a passo de montagem

Monte as duas metades em paralelo: a PCB é a mesma, mas cada lado usa uma face diferente como topo. Pense duas vezes, solde uma vez — dessoldar é difícil e arrisca danificar as trilhas.

1. **Prepare e marque as placas.** Separe as duas PCBs e marque com fita qual face será o topo de cada metade (esquerda e direita ficam espelhadas). Confira se todas as peças chegaram.
2. **Solde os diodos (face de baixo).** Os 58 diodos vão na parte de baixo da PCB. A listra fina é o catodo (–) e deve apontar para o lado da seta/barra na serigrafia; todos ficam na mesma orientação.
   1. Técnica: estanhe um pad, posicione o diodo com a pinça, reaqueça o pad, depois solde o outro lado.
3. **Solde os sockets hot-swap (face de baixo).** Mesmo lado dos diodos, seguindo o desenho da serigrafia. Pressione para que fiquem rentes à placa enquanto solda.
4. **Solde botão de reset e jack TRRS (face de cima).** Fixe com fita e solde por baixo.
5. **Faça as pontes de jumper do OLED.** Una com solda os 4 pares de pads de jumper na face de cima. Faça isso antes de montar o MCU: se ele for soldado direto, não dá para fazer depois.
6. **Prepare e monte o Pro Micro.** Use sockets (recomendado) ou solde direto.
   1. Na v2, a metade **esquerda** recebe o Pro Micro com a face limpa para cima (componentes voltados para a PCB).
   2. Na metade **direita**, ele fica com a face dos componentes para cima.
   3. Sockets fêmea vão na PCB; os pinos macho no Pro Micro. Não solde o MCU antes de conferir a orientação.
7. **Instale o socket do OLED.** Considere a altura do Pro Micro com os sockets que você usou; confira o encaixe antes de soldar.
8. **Primeiro teste.** Conecte MCU e OLED, grave o firmware (ver Firmware) e teste cada tecla fechando os contatos do socket com uma pinça ou pedaço de fio.
9. **Encoders (opcional).** Solde o EC11 em um, nos dois ou em nenhum lado. Limpe os resíduos de fluxo com álcool isopropílico.
10. **Switches e placas.** Encaixe os switches nos cantos da placa de topo primeiro, aparafuse os espaçadores, encaixe os switches com cuidado nos sockets (sem entortar os pinos) e complete o restante. Confira por baixo se todos os pinos entraram nos sockets.
11. **Feche o case.** Aparafuse a placa de fundo, coloque os keycaps e cole pelo menos 4 pés de borracha.

**Avisos:** nunca conecte ou desconecte o cabo TRRS com o teclado ligado ao USB (pode causar curto) — desconecte sempre o USB antes. Trate o conector USB do Pro Micro com cuidado: ele quebra com facilidade.

## Firmware

O Sofle v2 com fio usa QMK, cujo suporte já está no repositório oficial; para remapear sem recompilar, use a keymap `via` (app VIA) ou um build Vial.

**Gravação com QMK (Pro Micro / ATmega32U4):**

1. Instale o ambiente QMK ([guia para iniciantes](https://docs.qmk.fm/newbs)) ou use o QMK Toolbox / QMK MSYS no Windows.
2. Mantenha as metades **sem** o cabo TRRS.
3. Conecte uma metade por USB e rode, por exemplo:
   1. `qmk flash -kb sofle/rev1 -km default` (ou `-km via` para usar o app VIA)
   2. Pressione o botão de reset quando o terminal pedir (sem botão: encoste uma pinça nos pads RST e GND).
4. Repita na outra metade.
5. Desconecte o USB, ligue o cabo TRRS e conecte o USB na metade **esquerda**.

**Lateralidade (handedness):** por padrão, a metade ligada ao USB é a esquerda. Para poder ligar qualquer lado, grave cada metade com o bootloader indicando o lado, por exemplo `qmk flash -kb sofle/rev1 -km default -bl avrdude-split-left` e `...-bl avrdude-split-right` (use `dfu-split-*` no Elite-C).

**Remapeamento:**

- **VIA** ([usevia.app](https://usevia.app)): roda no navegador, remapeia teclas, camadas e encoders.
- **Vial** ([get.vial.today](https://get.vial.today)): fork do QMK com mais recursos em tempo real (combos, tap-dance); existem builds da comunidade para o Sofle.
- **ZMK** (só para versões sem fio com nice!nano): grava arrastando um arquivo `.uf2`; o ZMK Studio permite remapear sem recompilar.

Atenção: kits de alguns vendedores (como o Sofle RGB da Keyhive e o Sofle v2 da splitkb/Aurora) usam alvos de firmware próprios (`sofle/keyhive`, `splitkb/aurora/sofle_v2`); use sempre o firmware indicado pelo vendedor do seu PCB.

## Variações possíveis

As variações se dividem em versões de PCB (escolhidas antes de comprar) e escolhas de componentes (feitas sobre a mesma PCB).

**Versões de PCB da família Sofle** ([visão geral oficial](https://josefadamcik.github.io/SofleKeyboard/)):

| Versão | Switches | Iluminação | MCU | O que muda |
| --- | --- | --- | --- | --- |
| [Sofle v2](https://josefadamcik.github.io/SofleKeyboard/build_guide.html) | MX hot-swap | Nenhuma (só pads para fita LED) | Pro Micro | Base deste guia; MCU direito montado ao contrário do esquerdo |
| [Sofle RGB (v2.1)](https://josefadamcik.github.io/SofleKeyboard/build_guide_rgb.html) | MX hot-swap | Até 36 LEDs SK6812 mini por lado (por tecla + underglow + indicador) | Pro Micro | Stagger do mindinho mais suave; ambos os MCUs com componentes voltados à PCB; firmware `-km rgb_default` |
| [Sofle Choc](https://josefadamcik.github.io/SofleKeyboard/build_guide_choc.html) | Kailh Choc v1 hot-swap | RGB por tecla | Pro Micro | Perfil baixo, \~15 mm da mesa ao topo do keycap |
| [Sofle Pico](https://www.soflepico.com) | MX hot-swap | RGB por tecla | RP2040 Pico | Diodos THT ou SMD, OLED 128×64, gravação arrastando arquivo, furos para tenting |
| Aurora Sofle v2 ([splitkb](https://docs.splitkb.com)) | MX ou Choc | RGB | Pro Micro ou compatíveis (ex.: Liatris RP2040) | Redesenho comercial, firmware próprio (`splitkb/aurora/sofle_v2`) |
| Keyhive Sofle RGB | MX | RGB | Pro Micro | Fork incompatível com o firmware oficial; use guia e firmware da Keyhive |
| Sem fio (ex.: Sofle Hybrid, kits "wireless") | MX ou Choc | Opcional | nice!nano v2 (nRF52840) + bateria LiPo | Bluetooth, firmware ZMK; exige bateria e chave liga/desliga |

**Escolhas de componentes sobre a mesma PCB v2:**

- **Microcontrolador:** Pro Micro micro-USB (barato, porta frágil), Elite-C (USB-C, mesmo chip), ou clones RP2040 compatíveis com Pro Micro (USB-C, mais memória, gravação arrastando `.uf2`) usando o conversor do QMK (ex.: `-e CONVERT_TO=promicro_rp2040`). nice!nano funciona como substituto direto, mas exige ZMK e bateria.
- **Montagem do MCU:** soldado direto (mais baixo, permanente), sockets fêmea + pinos redondos (removível) ou spring pins (compactos e removíveis).
- **Telas:** OLED 128×32 em um, dois ou nenhum lado. Sem OLED em um lado, solde resistores pull-up de 4,7 kΩ (R1, R2) ou desative o OLED no firmware para evitar atraso na digitação.
- **Encoders:** EC11 em um, dois ou nenhum lado; no lugar do encoder pode ir um switch, dependendo da PCB.
- **Iluminação:** a v2 tem 3 pads (VCC, GND, dados) para ligar uma fita de LED RGB externa, configurada no firmware.
- **Case:** sanduíche (FR4, acrílico ou alumínio, espaçadores de 6–8 mm), tray case impresso em 3D ([exemplo no Printables](https://www.printables.com/model/268638-sofle-v2-case)), cases com tenting ou de madeira; espuma entre PCB e fundo reduz ruído.
- **Conexão entre metades:** TRRS (padrão) ou TRS; existe modificação com conector RJ12 ([Sofle V2 RJ12](https://gitlab.com/LayeredRx/Sofle_V2_Rj12/)).
- **Extras da comunidade:** trackball Pimoroni via I²C ([projeto](https://github.com/foureight84/sofle-keyboard-pimoroni)).

## Guia de switches e keycaps

O Sofle v2 usa sockets hot-swap MX, então qualquer switch com haste MX serve e dá para trocar depois sem soldar. Por isso, a escolha dos switches é sobre sensação e som, não sobre compatibilidade. Já nos keycaps, o formato importa mais por causa do layout em colunas.

### Tipos de switch

| Tipo | Sensação | Som | Indicado para |
| --- | --- | --- | --- |
| **Linear** | Curso liso, sem degrau, do topo ao fundo | Baixo a médio (vem do batente) | Jogos, digitação rápida, quem gosta de toque leve |
| **Tátil** | Um "degrau" perceptível perto do ponto de acionamento | Médio | Digitação longa: o degrau avisa que a tecla acionou |
| **Clicky** | Degrau tátil e um clique audível | Alto | Uso individual; incomoda em escritório ou chamadas |
| **Silencioso** (linear ou tátil) | Como os anteriores, com amortecedores na haste | Bem baixo | Escritório, ambiente compartilhado, gravação |
|  |  |  |  |

### O que olhar na especificação

- **Força de acionamento (gf):** de 35–45 gf é leve, 50–55 gf é médio e 60 gf ou mais é pesado. Num split como o Sofle, onde cada dedo tem sua coluna, switches leves a médios cansam menos os mindinhos.
- **Pré-curso e curso total:** o pré-curso padrão é de \~2 mm até acionar, com 4 mm de curso total. Switches "speed" acionam antes, por volta de 1,2 mm.
- **3 ou 5 pinos:** os 5 pinos têm dois pinos plásticos extras de estabilidade. Ambos encaixam no socket Kailh; se a PCB não tiver os furos laterais, basta cortar os pinos plásticos.
- **Materiais:** carcaça de policarbonato (PC) soa mais aguda e brilhante; nylon soa mais grave e abafado; haste de POM ou UPE é mais lisa. Os nomes "Milky", "Ink" e "Creamy" costumam indicar a mistura de materiais.
- **Pré-lubrificado de fábrica:** hoje é comum mesmo em modelos baratos e deixa o curso mais liso e menos arranhado.

### Modelos populares

| Modelo | Tipo | Força aprox. | Faixa | Observação |
| --- | --- | --- | --- | --- |
| Outemu Red / Outemu Sky | Linear | \~45 gf | Econômico | Bom para o primeiro teclado ou para aprender a lubrificar |
| Gateron Milky Yellow Pro (V2) | Linear | 50 gf | Econômico | A recomendação de custo-benefício mais citada pela comunidade |
| Akko V3 Cream Yellow / Creamy Black Pro | Linear | \~50 gf | Econômico | Som "creamy", vem lubrificado |
| Epomaker Creamy Jade | Linear | \~45 gf | Econômico | Pacotes de 90–110 unidades, som grave |
| Cherry MX Red / MX2A Red | Linear | 45 gf | Médio | O clássico de referência |
| Gateron Oil King (V2) | Linear | 55 gf | Premium | Muito liso e de som grave; entre os lineares mais bem avaliados |
| Cherry MX Brown | Tátil | 55 gf | Médio | Degrau suave; a opção "segura" para quem nunca usou tátil |
| Glorious Panda / HMX Jammy | Tátil | \~67 gf / médio | Premium | Degrau forte e nítido, para quem quer sentir bem cada tecla |
| Boba U4T | Tátil | 62 ou 68 gf | Premium | Degrau forte e som abafado |
| Akko V3 Penguin Silent | Tátil silencioso | \~50 gf | Econômico | Silencioso com degrau leve |
| Cherry MX Silent Red / TTC Silent Red | Linear silencioso | \~45 gf | Médio | Para escritório e gravação |
| Cherry MX Blue / Kailh Box White | Clicky | \~50–60 gf | Econômico a médio | O Box White tem clique mais limpo e menos chiado |

**Recomendações para o Sofle:**

- **Primeira montagem:** um linear econômico e pré-lubrificado, como o Gateron Milky Yellow Pro, ou um tátil leve, se você digita mais do que joga.
- **Na dúvida:** compre um *switch tester* (kit com 9–30 switches diferentes) antes de pedir 60 unidades do mesmo modelo.
- **Quantidade:** 58 switches mais reserva. A maioria vem em pacotes de 35, 70, 90 ou 110 unidades, então dois pacotes de 35 ou um de 70 resolvem.
- **Pesos diferentes:** como é hot-swap, dá para usar molas mais leves nas colunas do mindinho e mais firmes no resto.

### Perfis de keycap

O perfil é o formato e a altura da tecla. Nos perfis **esculpidos**, cada fileira (R1 a R4) tem altura e ângulo diferentes. Nos perfis **uniformes**, todas as teclas têm o mesmo formato e podem ir em qualquer posição.

| Perfil | Tipo | Altura aprox. | Formato do topo | No Sofle |
| --- | --- | --- | --- | --- |
| Cherry | Esculpido | \~9,4 mm | Cilíndrico | Funciona se você respeitar as fileiras; o mais comum em kits de qualidade |
| OEM | Esculpido | \~11,9 mm | Cilíndrico | O padrão de teclados prontos; mesmo cuidado com as fileiras |
| SA | Esculpido | \~16,5 mm | Esférico | Alto e retrô; pede apoio de pulso |
| MT3 | Esculpido | \~16,5 mm | Esférico fundo | Visual vintage, também alto |
| KAT | Esculpido | \~13,5 mm | Esférico | Entre Cherry e SA |
| ASA | Esculpido | entre OEM e SA | Esférico | Variante da Akko |
| **XDA** | **Uniforme** | **\~9,1 mm** | Esférico, topo largo | **Ótimo:** qualquer tecla em qualquer posição |
| **DSA** | **Uniforme** | **\~7,6 mm** | Esférico | **Ótimo:** baixo e fácil de completar |
| KAM | Uniforme | \~11 mm | Esférico | Versão uniforme do KAT |
| SLK | Uniforme | \~18% mais baixo que DSA | Côncavo | Feito para splits; vendido em kits "Ergo" |

**Por que o perfil uniforme é mais fácil no Sofle:**

- As teclas de polegar e a coluna extra de cada lado não existem num teclado comum. Com perfil uniforme, qualquer 1u serve em qualquer lugar.
- Com perfil esculpido, monte por fileira: R1 na fileira de números, R2 na de cima, R3 na do meio (onde ficam F e J), R4 na de baixo e nos polegares. Kits grandes têm 1u suficientes de cada fileira.

### Materiais e legendas

| Material | Toque | Durabilidade | Som |
| --- | --- | --- | --- |
| **ABS** | Liso | Fica brilhante com o uso | Mais agudo |
| **PBT** | Texturizado, seco | Não brilha, resiste bem | Mais grave |
| **POM** | Muito liso | Alta | Grave; raro e caro |

- **Doubleshot:** a legenda é uma segunda camada de plástico injetada e nunca apaga. Comum em ABS.
- **Dye-sub:** a tinta penetra no PBT e também não apaga, mas só funciona com legenda escura em tecla clara.
- **Laser ou impressão:** mais barato, pode desgastar com o tempo.
- **Sem legenda (blank):** comum em splits, porque o layout costuma ser personalizado com camadas.

### O que comprar para o Sofle

- **Composição:** 56 teclas 1u e 2 teclas 1.5u para os polegares externos, ou 58 de 1u. Garanta duas teclas com marcação de posição (homing) para F e J.
- **Haste:** cruz MX ("Cherry MX compatível"). Keycaps para Choc ou de perfil baixo Choc não encaixam.
- **Kits indicados:** kits "Ergo", "40%" ou "Ortho", que trazem muitas 1u e algumas 1.5u; kits XDA ou DSA em PBT (blank ou dye-sub) do AliExpress, com mais de 100 teclas; ou um kit Cherry completo (104 a 140 teclas), usando as 1u de cada fileira.
- **Impressão 3D:** como você já imprime, existem modelos com haste MX prontos para imprimir, como o FormKey no MakerWorld. Imprima com o topo para cima e teste o encaixe da haste antes de imprimir o conjunto.

## Case impresso em 3D

O modelo recomendado é o **[Pehmis Sofle Case](https://github.com/Pelicram/Pehmis-Sofle-Case)**, de Pelicram. É um case fechado, sem frestas, com apoios de pulso magnéticos, derivado do [SofleCase de kb-elmo](https://github.com/str-dst/SofleCase). Ele combina com as peças deste projeto:

- **Compatibilidade:** feito para a PCB Sofle **v2.0** (não serve para a v2.1 com RGB por tecla).
- **Pro Micro:** tem espaço para um Pro Micro comum montado em socket.
- **Knob:** o knob incluído foi feito para EC11 com eixo **Plum de 15 mm**, o mesmo comprado.
- **Espaçadores:** usa os mesmos espaçadores M2 × 8 mm.

O Pehmis usa montagem tipo *tray*: a PCB com a placa de switches é aparafusada no fundo do case. **Ele não inclui a placa de switches**, que você imprime a partir do arquivo oficial (veja abaixo). A licença é CC BY-NC-SA 4.0: uso pessoal liberado, venda proibida.

### Arquivos e peças

Os arquivos ficam no repositório, nas pastas `3MF` (já orientados para impressão) e `STEP` (para editar em CAD).

| Peça | Qtd. | Função |
| --- | --- | --- |
| `L-Top` / `R-Top` | 1 de cada | Carcaça superior; recebe os insertos roscados e os ímãs |
| `L-Bottom` / `R-Bottom` | 1 de cada | Fundo (tray), onde a PCB é aparafusada |
| `L-Wristrest` / `R-Wristrest` | 1 de cada | Apoios de pulso magnéticos (opcionais) |
| `Knob` | 2 | Knob para EC11 com eixo Plum de 15 mm |
| Placa de switches | 2 | Não incluída no Pehmis; arquivo pronto na pasta do projeto, em 01-placa-switches |

As metades esquerda e direita **não são simétricas**, porque os furos de USB e TRRS mudam de posição. Imprima os dois arquivos; não espelhe um no fatiador.

### Material extra

| Item | Qtd. | Situação |
| --- | --- | --- |
| Espaçadores M2 × 8 mm | 10 | ✅ Já comprado |
| Parafusos M2 × 4 mm (placa e PCB no fundo) | 20 | ✅ No kit de parafusos |
| Parafusos M2 × 8 mm (fecham o case) | 10 | Confira no kit de parafusos |
| Insertos roscados M2 × 4 × 3,5 mm (*heat-set*) | 10 | ❌ Comprar |
| Ímãs de neodímio 8 × 3 mm | 8 | ❌ Comprar, se for usar os apoios de pulso |
| Pés de borracha de 8 mm | 16 | 🖨️ Imprimir discos de 8 mm em TPU (os encaixes do case são de 8 mm) |
| Cola instantânea (cianoacrilato) ou epóxi | — | Para fixar os ímãs |

### Como imprimir o case

- **Arquivos:** use os 3MF da pasta `3MF`. Eles já vêm orientados e não precisam de suporte.
- **Material:** PETG ou PLA. O PETG aguenta melhor o calor, como num carro ao sol; o PLA é mais fácil e tem acabamento melhor.
- **Camadas:** 0,2 mm.
- **Paredes:** 3 a 4, para que os furos dos insertos e parafusos fiquem firmes.
- **Topo e fundo:** 4 a 5 camadas sólidas.
- **Preenchimento:** 15–25%.
- **Mesa:** a de PEI liso deixa as faces apoiadas mais bonitas. Use brim se as peças grandes tenderem a descolar nos cantos.
- **Cor:** imprima topo e fundo da mesma cor para um visual contínuo, ou em cores diferentes para destacar o fundo.

### Como imprimir a placa de switches

A placa de switches é a peça mais crítica: ela trava e alinha os switches, então as medidas precisam ser exatas.

**Arquivo pronto:** a placa já foi gerada a partir do Gerber oficial e está na pasta do projeto, em `01-placa-switches` (furos de 14,0 mm e de 14,1 mm, mais a tira de teste). Os passos 1 a 3 abaixo só são necessários se você quiser refazer o modelo no CAD.

1. **Obtenha o desenho.** Baixe o [`v2-gerber-top.zip`](https://github.com/josefadamcik/SofleKeyboard/releases/download/v2.0.1/v2-gerber-top.zip) da versão v2.0.1. Abra-o no GerbView do KiCad (gratuito) e exporte o contorno, que inclui os furos dos switches, como DXF. Outra opção é usar um conversor online de Gerber para DXF.
2. **Extrude no CAD.** Importe o DXF no Fusion, Onshape, FreeCAD ou Tinkercad e extrude **1,5 mm**. Essa é a espessura em que as travas do switch MX encaixam: mais grossa, o switch não trava; mais fina, ele fica solto.
   1. **Opção mais rígida:** extrude 3 mm e faça, por baixo de cada furo, um rebaixo de \~15 × 15 mm, deixando só 1,5 mm de material na face de cima.
3. **Confira o modelo.** Devem aparecer 29 furos de 14 × 14 mm, os furos dos espaçadores e o recorte do encoder nas posições da placa original.
4. **Faça um teste de tolerância.** Antes da placa inteira, imprima uma tira de 1,5 mm com 3 furos de 14,0, 14,1 e 14,2 mm. Use a medida em que o switch encaixa com um clique e fica firme, e ajuste os furos no CAD se precisar.
5. **Imprima duas placas.** A placa original é reversível, então imprima uma normal e outra **espelhada no fatiador**, uma para cada metade.
6. **Configure a impressão:**
   1. **Material:** PETG ou PLA+, que flexionam menos que o PLA comum.
   2. **Posição:** deitada, com a face de cima voltada para a mesa, para que essa face fique lisa e os furos precisos.
   3. **Preenchimento:** 100%, sólido. Em 1,5 mm, isso deixa a placa sem vazios.
   4. **Altura de camada:** um valor que divida 1,5 mm exatamente, como 0,15 ou 0,25 mm, para a espessura sair certa.
   5. **Pé de elefante:** ative a compensação de primeira camada (0,1–0,15 mm). Sem ela, a primeira camada sai mais larga e estreita os furos justamente onde o switch trava.
7. **Faça o acabamento.** Remova o brim e passe um estilete nos cantos dos furos se algum switch entrar apertado.

A placa impressa flexiona um pouco mais que a de FR4. Com os 10 espaçadores no lugar, isso quase não se nota na digitação, mas segure a placa ao puxar um switch com o extrator, para não forçar o socket hot-swap da PCB.

### Como montar

1. **Solde o botão de reset por baixo da PCB.** Isso muda o passo 4 da montagem: com o botão por baixo, ele fica acessível pelo furo no fundo do case, sem desmontar o teclado.
2. **Monte o teclado normalmente:** PCB, espaçadores M2 × 8 mm, placa de switches impressa e switches. Não instale a placa de fundo FR4.
3. **Instale os insertos roscados** nos furos de `L-Top` e `R-Top`. Aqueça o inserto com o ferro de solda e empurre na vertical até ficar rente, a \~200–220 °C para PLA ou \~230–240 °C para PETG.
4. **Aparafuse cada metade no fundo:** a PCB com a placa vai em `L-Bottom` ou `R-Bottom`, com os parafusos M2 × 4 mm.
5. **Feche o case:** encaixe cada fundo no topo correspondente e aparafuse com os M2 × 8 mm.
6. **Coloque os knobs** nos encoders.
7. **Cole os ímãs** nos furos de `L-Top`, `R-Top`, `L-Wristrest` e `R-Wristrest`. Antes de colar, marque a polaridade com caneta, para que cada par se atraia em vez de se repelir.
8. **Coloque os pés** de 8 mm nos encaixes do fundo.

### Alternativas

- **[SofleCase de kb-elmo](https://github.com/str-dst/SofleCase):** o único case 100% impresso que inclui a placa de switches (topo, placa, fundo e knob). Foi feito para Elite-C e Puchi-C, e o autor avisa que o furo do USB não alinha direito com um Pro Micro comum.
- **[Sofle v2 case (Printables 268638)](https://www.printables.com/model/268638-sofle-v2-case):** só o fundo (tray), com os mesmos espaçadores de 8 mm. Exige a placa FR4 ou uma placa impressa.
- **[Sofle V2 (non-RGB) tenting case (Printables 615335)](https://printables.com/model/615335-sofle-v2-non-rgb-tenting-case):** só o fundo, com tenting de 21°. Pede espaçadores de 7 mm e o Pro Micro em socket.
- **Não servem para a v2:** os cases feitos para o Sofle RGB/v2.1, o Sofle Choc ou o Sofle Pico, cujos contornos são diferentes.

## Solução de problemas

A maioria das falhas vem de solda fria, diodo invertido ou MCU na orientação errada — teste antes de fechar o case.

| Sintoma | Causa provável | O que fazer |
| --- | --- | --- |
| Uma tecla não funciona | Solda fria no socket ou no diodo; diodo invertido | Refaça a solda; confira a listra do diodo contra a serigrafia; teste o socket com pinça |
| Uma linha ou coluna inteira falha | Pino do MCU mal soldado ou socket com mau contato | Refaça a solda do pino correspondente; teste continuidade com multímetro |
| Metade direita não responde | Cabo TRRS solto/defeituoso, jack mal soldado ou firmware diferente nas metades | Grave o mesmo firmware nas duas; troque o cabo; revise o jack |
| Lado esquerdo e direito trocados | Lateralidade definida pelo USB | Ligue o USB à esquerda ou grave com `-bl avrdude-split-left/right` |
| OLED não liga | Pontes de jumper do OLED não feitas; display ao contrário | Faça as 4 pontes; confira a ordem GND/VCC/SCL/SDA |
| Atraso na digitação sem OLED em um lado | Faltam pull-ups no I²C | Solde resistores de 4,7 kΩ em R1/R2 ou desative o OLED no firmware |
| Encoder gira ao contrário | Pinos A/B invertidos no firmware | Inverta a direção na keymap ou no VIA/Vial |
| Elite-C v3.0 instável no split | Bug da revisão 3.0 | Adicione `#define SPLIT_USB_DETECT` ao `config.h` (corrigido na v3.1) |
| Teclado reinicia ou trava ao mexer no cabo | TRRS conectado com USB ligado | Sempre desconecte o USB antes de mexer no TRRS |

Se o MCU for soldado direto e estiver com defeito, a troca é difícil — mais um motivo para usar sockets.

## Onde comprar no Brasil e dicas

Kits completos são raros no varejo nacional; o caminho mais comum é comprar PCB e peças importadas e completar com eletrônicos genéricos locais.

- **Kit completo importado:** AliExpress e lojas como beekeeb, KeebMaker, Mechboards ou splitkb vendem kits Sofle v2/RGB, com ou sem solda prévia. Confira se o kit é v2, v2.1 RGB ou fork (Keyhive), pois o firmware muda.
- **PCB sob encomenda:** envie os Gerbers do GitHub a um fabricante como JLCPCB ou PCBWay (2 camadas, 1,6 mm). O pedido mínimo costuma ser 5 placas — dá para dividir com amigos.
- **Eletrônicos genéricos:** Pro Micro, OLED SSD1306, encoder EC11, jack PJ-320A, botões táteis e diodos 1N4148W são encontrados no Mercado Livre e em lojas de eletrônica/Arduino nacionais, geralmente com entrega mais rápida.
- **Switches e keycaps:** comunidades e lojas de teclados mecânicos nacionais vendem switches MX e keycaps; confirme que os keycaps tenham duas 1.5u ou use só 1u.
- **Impostos:** compras internacionais pagam imposto de importação e ICMS; verifique as regras vigentes antes de dividir ou juntar pedidos.
- **Dica de primeira montagem:** prefira um MCU RP2040 compatível com Pro Micro (USB-C, menos frágil) e use sockets — facilita trocar o controlador se algo der errado.

## Referências e fontes

Páginas consultadas na pesquisa deste guia (acesso em outubro de 2026).

**Documentação oficial do Sofle**

- [SofleKeyboard — página principal e versões](https://josefadamcik.github.io/SofleKeyboard/)
- [Guia de montagem v1/v2](https://josefadamcik.github.io/SofleKeyboard/build_guide.html)
- [Guia de montagem RGB](https://josefadamcik.github.io/SofleKeyboard/build_guide_rgb.html)
- [Guia de montagem Choc](https://josefadamcik.github.io/SofleKeyboard/build_guide_choc.html)
- [Guia de montagem Pico (soflepico.com)](https://www.soflepico.com)
- [Compra de peças (sourcing)](https://josefadamcik.github.io/SofleKeyboard/sourcing_parts.html)
- [Repositório GitHub (KiCad, Gerbers, cases)](https://github.com/josefadamcik/SofleKeyboard)
- [Releases com Gerbers](https://github.com/josefadamcik/SofleKeyboard/releases)

**Firmware**

- [QMK — guia para iniciantes](https://docs.qmk.fm/newbs)
- [QMK — teclados split e lateralidade](https://docs.qmk.fm/features/split_keyboard)
- [VIA](https://usevia.app) · [Vial](https://get.vial.today)
- [Keymap VIA da Keyhive para o Sofle](https://git.ahoneybun.net/ahoneybun/qmk_firmware/src/commit/f9abecda3f21dfdbf5da29571cf966d1a3184f08/keyboards/sofle/keymaps/keyhive_via)
- [Suporte Vial para o Sofle (commit da comunidade)](https://github.com/rizalfr/qmk_firmware/commit/4d4afd4fe17c5933f131509fd4ab896f8f3498db)
- [ZMK config para Sofle sem fio (exemplo)](https://github.com/mctechnology17/zmk-config)
- [Sofle Hybrid Ergomech (ZMK, nice!nano)](https://github.com/ergomechstore/sofle-hybrid-ergomech)

**Guias de vendedores e da comunidade**

- [KeebMaker — Sofle Build Guide](https://keebmaker.com/pages/km-sofle-build-guide)
- [KeebsForAll — Complete Sofle V2 Build & Soldering Guide (2025)](https://keebsforall.com/blogs/mechanical-keyboards-101/complete-sofle-v2-build-soldering-guide)
- [Mechboards — vídeo de montagem do Sofle V2 (YouTube)](https://www.youtube.com/watch?v=_3pe236--hA)
- [splitkb — documentação da série Aurora](https://docs.splitkb.com)
- [splitkb — como colocar sockets no microcontrolador](https://docs.splitkb.com/hc/en-us/articles/360011263059)
- [Flare576/sofle — relato de montagem de iniciante](https://github.com/Flare576/sofle)
- [KBD.news — lançamento oficial do Sofle v2 (jan/2021)](https://kbd.news/Sofle-v2-officialized-132.html)

**Modificações e acessórios**

- [Tray case para Sofle v2 (Printables)](https://www.printables.com/model/268638-sofle-v2-case)
- [Sofle V2 com conector RJ12](https://gitlab.com/LayeredRx/Sofle_V2_Rj12/)
- [Integração de trackball Pimoroni](https://github.com/foureight84/sofle-keyboard-pimoroni)
- [nice!nano (KeebMaker)](https://keebmaker.com/products/nice-nano-wireless-controller)

**Switches e keycaps**

- [Keebio — guia de seleção de keycaps para splits](https://blog.keeb.io/keycap-selection-guide/)
- [Das Keyboard — comparação de perfis de keycap](https://www.daskeyboard.com/blog/?p=9556)
- [Angry Miao — perfis de keycap explicados](https://store.angrymiao.com/blogs/insider-stories/keycap-profiles-explained)
- [Wooting — keycap profiles explained](https://help.wooting.io/article/152-keycap-profiles-explained)
- [splitkb — SLK PBT Ergo Blanks](https://splitkb.com/products/slk-pbt-blanks)
- [KBD.news — banco de dados de switches MX](https://kbd.news/switch/MX)
- [FormKey — keycaps MX para impressão 3D (MakerWorld)](https://makerworld.com/es/models/1455091-formkey-a-fully-3d-printed-keycap-set)
