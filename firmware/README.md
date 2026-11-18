# Firmware

Firmware QMK para o Sofle v2 original (`sofle/rev1`) com os Pro Micro USB-C deste projeto.

## Arquivos

| Caminho | O que é |
| --- | --- |
| `build/sofle_rev1_afm.hex` | **Firmware principal**: layout pessoal AFM (ABNT2) + `SPLIT_USB_DETECT` |
| `build/sofle_rev1_via_usbdetect.hex` | Alternativa: layout padrão com VIA (remapeável no navegador) + `SPLIT_USB_DETECT` |
| `keymaps/afm/` | Fonte do layout AFM: `keymap.json` (layout, editável no QMK Configurator), `keymap.c` (encoders: volume/Mute e rolagem/Home), `config.h` |
| `keymaps/via-usbdetect/` | Fonte do keymap VIA (de `the-via/qmk_userspace_via`) com `config.h` |

## Por que `SPLIT_USB_DETECT`

Nestes clones de Pro Micro, a energia que chega pelo TRRS também aparece no pino que o QMK usa para detectar o USB (VBUS). Com o firmware padrão, as **duas** metades se acham ligadas ao computador, e a metade sem cabo USB não funciona. `SPLIT_USB_DETECT` faz cada metade só se considerar ligada ao USB quando o computador realmente conversa com ela. Consequência: a metade sem USB leva cerca de 2 s para começar a funcionar ao ligar.

Por isso, **não use o `.hex` gerado direto pelo [QMK Configurator](https://config.qmk.fm)**: ele não inclui o `config.h`.

## Atenção ao alvo

Use sempre `sofle/rev1`. O alvo `splitkb/aurora/sofle_v2/rev1` (Aurora Sofle, da splitkb) tem **outros pinos de matriz** e usa o pino F4 para lateralidade, que nesta PCB é o encoder. Um firmware Aurora não funciona nesta placa.

## Gravar (uma metade por vez, sem o cabo TRRS)

No QMK MSYS, na raiz do repositório:

```sh
qmk flash firmware/build/sofle_rev1_afm.hex
```

Quando aparecer a mensagem de espera do bootloader, dê o reset duplo (dois toques rápidos em RST-GND). O sucesso termina com `20590 bytes of flash verified`. Depois: TRRS ligado com o USB desconectado, e o USB na metade **esquerda**.

Pelo QMK Toolbox: abra o `.hex`, MCU `ATmega32U4`, **Auto-Flash** ligado e reset duplo. Se a linha `Caterina device connected` terminar em `[]` (sem a porta), nada foi gravado: repita.

## Recompilar

No QMK MSYS, na raiz do repositório, `make` faz tudo abaixo (copia o keymap, compila e atualiza `build/sofle_rev1_afm.hex`) e `make flash` grava. Use `make help` para ver os alvos; se o QMK não estiver em `~/qmk_firmware`, passe `QMK_HOME=...`.

Passo a passo manual, se preferir:

```sh
cp -r firmware/keymaps/afm "$QMK_HOME/keyboards/sofle/keymaps/afm"
qmk compile -kb sofle/rev1 -km afm
cp "$QMK_HOME/sofle_rev1_afm.hex" firmware/build/
```

Detalhes gerais (lateralidade, VIA/Vial, drivers no Windows): [docs/07-firmware.md](../docs/07-firmware.md).
