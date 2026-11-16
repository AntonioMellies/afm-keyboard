# Pedido da PCB

> Parte da documentação de referência do projeto. Para marcar o que já foi feito, use `PROGRESS.md` (veja o [README](../README.md)).

## Arquivos

Os Gerbers oficiais da **v2.0.1** (sem RGB) estão em [`hardware/pcb/gerbers/`](../hardware/pcb/gerbers/):

| Arquivo | Uso |
| --- | --- |
| `v2-gerber-pcb.zip` | PCB principal. **Envie este zip sem descompactar** ao fabricante |
| `v2-gerber-top.zip` | Placa de topo (aqui usada só como base da placa de switches impressa) |
| `v2-gerber-bottom.zip` | Placa de fundo (não usada: o fundo é o tray impresso do case) |

Fonte oficial: [releases do SofleKeyboard](https://github.com/josefadamcik/SofleKeyboard/releases).

## Parâmetros do pedido (JLCPCB)

- Material: FR-4, **2 camadas**, espessura **1,6 mm**
- Acabamento: **LeadFree HASL**
- Máscara/serigrafia: preto/branco (preferência estética)
- Via Tented
- Quantidade: 5 unidades (mínimo; 2 são usadas, a mesma placa serve aos dois lados)

## Conferência na prévia

A prévia do fabricante deve mostrar o Pro Micro com furos desencontrados entre as duas metades, característica da v2.

Topo e fundo **não** são fabricados em FR-4 neste projeto: são impressos em 3D ([Impressão 3D](05-3d-printing.md)).

Mais informações: [Materiais](02-bom.md) e [Referências](10-references.md).
