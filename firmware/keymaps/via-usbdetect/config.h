#pragma once
// Detecta o USB pela enumeração, não pela tensão em VBUS.
// Necessário em clones de Pro Micro que alimentam VBUS pelo pino VCC (TRRS).
#define SPLIT_USB_DETECT
#define SPLIT_USB_TIMEOUT 2000
#define SPLIT_USB_TIMEOUT_POLL 10
