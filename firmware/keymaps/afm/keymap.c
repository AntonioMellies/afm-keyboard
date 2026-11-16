// Código extra do keymap. O layout vem do keymap.json; o QMK inclui este
// arquivo automaticamente junto com ele.
//
// Encoders iguais em todas as camadas.
// Esquerdo (índice 0): volume. Direito (índice 1): rolagem do mouse.
// Os cliques ficam no keymap.json: esquerdo = KC_MUTE, direito = KC_HOME.
#include QMK_KEYBOARD_H

bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) {
        tap_code(clockwise ? KC_VOLU : KC_VOLD);
    } else if (index == 1) {
        tap_code(clockwise ? MS_WHLD : MS_WHLU);
    }
    return false; // impede o comportamento padrão do sofle.c (PgUp/PgDn)
}
