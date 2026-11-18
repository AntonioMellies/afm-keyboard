# Keymap `afm`

Layout pessoal (ABNT2) para o Sofle v2 original (`sofle/rev1`), com três camadas:

| Camada | Ativação | Conteúdo |
| --- | --- | --- |
| 0 | — | Base QWERTY ABNT2 (`KC_NUBS`, `KC_INT1`, `KC_RBRC`); Tab no mindinho esquerdo (linha 2), `'` na borda da home row esquerda; Espaço no polegar esquerdo interno e Enter no direito interno; no polegar direito, `-` e `=` nas duas teclas mais externas |
| 1 | `MO(1)` (polegar esquerdo) | F1–F12, teclado numérico na mão direita com Num Lock à esquerda do 7, Caps Lock (onde fica o Tab na base), `\` (borda da home row esquerda); Copiar e Colar (Ctrl+C e Ctrl+V) nas teclas D e F (home row esquerda) |
| 2 | `MO(2)` (polegar direito) | Setas (inverted-T em I/J/K/L), Home (H, à esquerda da seta ←) e End (`'`, à direita da seta →), mídia, Insert/Delete, Print Screen |

Shift e Ctrl esquerdos funcionam em todas as camadas (`KC_TRNS` nas camadas 1 e 2), então `Shift` + setas/Home/End seleciona texto com a camada 2 segurada.

## Encoders (iguais nas três camadas)

| Encoder | Girar | Clicar |
| --- | --- | --- |
| Esquerdo | Volume (horário aumenta) | Mute (`KC_MUTE`) |
| Direito | Rolagem do mouse (horário desce) | Home (`KC_HOME`) |

## Arquivos

- `keymap.json` — **fonte do layout**. Pode ser importado e editado no [QMK Configurator](https://config.qmk.fm) com o teclado `sofle/rev1`; exporte e substitua este arquivo.
- `keymap.c` — só o código dos encoders. O QMK inclui este arquivo automaticamente junto com o `keymap.json`; não coloque o layout aqui.
- `config.h` — liga `SPLIT_USB_DETECT` (ver `../../README.md`).

Ao editar no Configurator, mantenha `KC_MUTE` e `KC_HOME` nas posições dos cliques dos encoders em todas as camadas.

## Compilar

Na raiz do repositório, no QMK MSYS: `make` (compila e atualiza o `.hex`) e `make flash` (grava). Manualmente:

```sh
cp -r firmware/keymaps/afm "$QMK_HOME/keyboards/sofle/keymaps/afm"
qmk compile -kb sofle/rev1 -km afm
cp "$QMK_HOME/sofle_rev1_afm.hex" firmware/build/
```

Não use o `.hex` gerado pelo site do Configurator: ele não inclui o `config.h` nem o `keymap.c`.
