# Firmware


> Parte da documentação de referência do projeto. Para marcar o que já foi feito, use `PROGRESS.md` (veja o [README](../README.md)).

O Sofle v2 com fio usa QMK, cujo suporte já está no repositório oficial; para remapear sem recompilar, use a keymap `via` (app VIA) ou um build Vial.

**Gravação com QMK (Pro Micro / ATmega32U4):**

1. Instale o ambiente QMK ([guia para iniciantes](https://docs.qmk.fm/newbs)) ou use o QMK Toolbox / QMK MSYS no Windows.
2. Mantenha as metades **sem** o cabo TRRS.
3. Conecte uma metade por USB e rode `qmk flash firmware/build/sofle_rev1_afm.hex` (firmware deste projeto; veja [firmware/README.md](../firmware/README.md)).
   1. Dê o **reset duplo** (dois toques rápidos em RST-GND) quando o terminal pedir. Com um toque só, o bootloader destes clones fica ativo por menos de 1 s.
4. Repita na outra metade.
5. Desconecte o USB, ligue o cabo TRRS e conecte o USB na metade **esquerda**.

**Lateralidade (handedness):** por padrão, a metade ligada ao USB é a esquerda. Para poder ligar qualquer lado, grave cada metade com o bootloader indicando o lado, por exemplo `qmk flash -kb sofle/rev1 -km default -bl avrdude-split-left` e `...-bl avrdude-split-right` (use `dfu-split-*` no Elite-C).

**Remapeamento:**

- **VIA** ([usevia.app](https://usevia.app)): roda no navegador, remapeia teclas, camadas e encoders.
- **Vial** ([get.vial.today](https://get.vial.today)): fork do QMK com mais recursos em tempo real (combos, tap-dance); existem builds da comunidade para o Sofle.
- **ZMK** (só para versões sem fio com nice!nano): grava arrastando um arquivo `.uf2`; o ZMK Studio permite remapear sem recompilar.

**Pro Micro clone e `SPLIT_USB_DETECT`:** com os Pro Micro USB-C deste projeto, o firmware padrão (`-km default`, `-km via` ou o `.hex` do QMK Configurator) deixa a metade sem USB inoperante, porque a energia do TRRS chega ao pino de detecção de USB. Use os firmwares de `firmware/build/`, compilados com `#define SPLIT_USB_DETECT`.

**Drivers no Windows:** o bootloader precisa aparecer como **"Dispositivo Serial USB"** com provedor **Microsoft**. O driver antigo da Arduino (`arduino.inf`, versão 1.2.3.0 de 2015) causa erros `ser_send(): write error` e `butterfly_recv(): programmer is not responding`. Para removê-lo, liste os pacotes com `pnputil /enum-drivers` em um terminal de administrador e apague os da Arduino com `pnputil /delete-driver oemXX.inf /uninstall /force`. Reinstalar o Arduino IDE ou rodar "Install Drivers" no QMK Toolbox pode trazê-lo de volta.

Atenção: kits de alguns vendedores (como o Sofle RGB da Keyhive e o Sofle v2 da splitkb/Aurora) usam alvos de firmware próprios (`sofle/keyhive`, `splitkb/aurora/sofle_v2`); use sempre o firmware indicado pelo vendedor do seu PCB. Um firmware `splitkb/aurora/sofle_v2` **não funciona** na PCB original v2.0.1: os pinos da matriz são outros.
