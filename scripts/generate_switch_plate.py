"""Gera a placa de switches do Sofle v2 em 3MF a partir do Gerber oficial (v2.0.1).

Uso (na raiz do repositório):
    pip install -r requirements.txt
    python scripts/generate_switch_plate.py [pasta_de_saida]

Entrada: hardware/switch-plate/gerbers-top/ (Gerber do topo, v2.0.1; veja scripts/parse_gerber.py).
Saída padrão: hardware/switch-plate/out/
Para outros tamanhos de furo, edite a lista HOLE_SIZES.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import trimesh
from shapely.geometry import Polygon, Point, box
from shapely.affinity import translate
from parse_gerber import build

THICK = 1.5          # espessura em que as travas do switch MX encaixam
SCREW_D = 2.4        # furo M2 (Gerber = 2,2; +0,2 de folga para impressão)
HOLE_SIZES = (14.0, 14.1, 14.2)   # tamanhos de furo gerados (mm)
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "hardware", "switch-plate", "out")

outer, inner, holes = build()
switches = [p for p in inner if abs(p.area - 196) < 1]
encoder = [p for p in inner if abs(p.area - 196) >= 1]
assert len(switches) == 29 and len(encoder) == 1, (len(switches), len(encoder))

minx, miny, _, _ = outer.bounds

FILLET = 0.3         # raio nos cantos dos furos e do contorno (alivia concentração de tensão)

def plate(cut):
    d = (cut - 14.0) / 2
    cuts = [s.buffer(d, join_style="mitre") if d else s for s in switches]
    cuts += encoder
    cuts += [Point(x, y).buffer(SCREW_D / 2, 64) for x, y, _ in holes]
    shape = outer
    for c in cuts:
        shape = shape.difference(c)
    shape = shape.buffer(FILLET, 32).buffer(-FILLET, 32)     # arredonda cantos dos furos (côncavos)
    shape = shape.buffer(-FILLET, 32).buffer(FILLET, 32)     # arredonda cantos do contorno (convexos)
    shape = translate(shape, -minx, -miny).buffer(0).simplify(0.005, preserve_topology=True)
    return trimesh.creation.extrude_polygon(shape, THICK)

# O Bambu Studio exige um projeto completo (impressora + filamento), então o perfil vai em texto, não dentro do 3MF.
PRINT_NOTES = """Placa de switches - ajustes no Bambu Studio (PLA)

Base: perfil "Fine 0.12mm" do 0.4 mm + "Bambu PLA Basic" (ou PLA genérico).
Não mexa em velocidades, aceleração, temperatura ou ventoinha: os padrões do
perfil são rápidos e já corretos para PLA. Só altere o que está listado abaixo.

Posição: deitada (como importada), 1,5 mm de altura. Sem suportes, sem brim.

Qualidade
  Altura de camada ........ 0,12 mm (~12 camadas)

Resistência
  Loops de parede ......... 4
  Densidade de preench. ... 100%
  Padrão de preenchimento . Retilíneo (Rectilinear)
  Camadas sólidas topo/base padrão do perfil (com 100% de preenchimento tanto faz)

Tempo
  A placa tem ~8 cm3 de PLA. Com 0,12 mm e as velocidades padrão do Bambu
  (sem reduzi-las à mão), leva mais que com 0,20 mm; confira a estimativa
  no fatiador.

Dicas para PLA
  - PLA é mais quebradiço que PETG: mexa no encaixe dos switches com calma.
  - Use filamento seco; PLA úmido enfraquece muito a peça.
  - Se ainda ficar frágil, peça a versão de 2,0 mm.
"""

def export(mesh, name):
    path = os.path.join(OUT, name)
    mesh.export(path)
    back = trimesh.load(path, force="mesh")
    print(f"{name}: watertight={back.is_watertight} bounds={back.extents.round(2)} vol={back.volume:.0f}mm3")

def test_strip():
    # tira de 1,5 mm com furos 14,0 / 14,1 / 14,2 mm; marcadores de 1 a 3 furinhos indicam o tamanho
    pitch, w, h = 21.0, 3 * 21.0 + 4, 26.0
    shape = box(0, 0, w, h)
    for i, s in enumerate((14.0, 14.1, 14.2)):
        cx, cy = 2 + pitch / 2 + i * pitch, 15.0
        shape = shape.difference(box(cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2))
        for k in range(i + 1):
            shape = shape.difference(Point(cx - (i) * 1.5 + k * 3.0, 3.5).buffer(0.9, 32))
    return trimesh.creation.extrude_polygon(shape, THICK)

os.makedirs(OUT, exist_ok=True)
for size in HOLE_SIZES:
    export(plate(size), f"switch-plate_{size:.1f}mm.3mf")
open(os.path.join(OUT, "print-settings_bambu_PLA.txt"), "w", encoding="utf-8").write(PRINT_NOTES)
export(test_strip(), "tolerance-test_14.0-14.2mm.3mf")
