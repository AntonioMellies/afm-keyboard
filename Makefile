# Atalhos para compilar e gravar o firmware AFM.
# Rode no QMK MSYS, na raiz do repositório: `make`, `make flash`, `make help`.

KEYBOARD  ?= sofle/rev1
KEYMAP    ?= afm
QMK_HOME  ?= $(HOME)/qmk_firmware

# Os keymaps ficam na pasta do teclado-base (sofle), não na da revisão (rev1).
KB_BASE   := $(firstword $(subst /, ,$(KEYBOARD)))
SRC_DIR   := firmware/keymaps/$(KEYMAP)
DEST_DIR  := $(QMK_HOME)/keyboards/$(KB_BASE)/keymaps/$(KEYMAP)
HEX_NAME  := $(subst /,_,$(KEYBOARD))_$(KEYMAP).hex
HEX_OUT   := firmware/build/$(HEX_NAME)

.PHONY: build flash sync help

build: sync ## Compila o keymap e copia o .hex para firmware/build/
	qmk compile -kb $(KEYBOARD) -km $(KEYMAP)
	cp "$(QMK_HOME)/$(HEX_NAME)" "$(HEX_OUT)"
	@echo "Pronto: $(HEX_OUT)"

flash: ## Grava o .hex já compilado (uma metade por vez, sem TRRS; reset duplo ao pedir)
	qmk flash $(HEX_OUT)

sync: ## Copia o keymap do repositório para o QMK_HOME
	@test -d "$(QMK_HOME)" || { echo "QMK_HOME não encontrado: $(QMK_HOME)"; exit 1; }
	rm -rf "$(DEST_DIR)"
	cp -r $(SRC_DIR) "$(DEST_DIR)"

help: ## Mostra esta ajuda
	@grep -E '^[a-z]+:.*## ' $(MAKEFILE_LIST) | sed -E 's/^([a-z]+):.*## (.*)/  make \1\t\2/'
