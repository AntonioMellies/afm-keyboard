"""Gera o knob do encoder EC11 com eixo Plum de 15 mm a partir do Knob-X2 do Pehmis.

Uso (na raiz do repositório):
    pip install -r requirements.txt
    python scripts/generate_knob.py [pasta_de_saida]

Entrada: hardware/case-pehmis/3mf/Knob-X2.3mf (cópia de terceiros, nunca é alterada).
Saída padrão: hardware/knob-plum/Knob-X2_plum15_bore-<d>mm.3mf (um arquivo com um objeto
nomeado por diâmetro de BORE_SIZES; hoje só Ø5,9) + tira de teste de encaixe.

O que muda em relação ao original (só o furo do eixo; a forma externa e as alturas ficam iguais):
  - Furo do eixo: Ø6,1 mm liso -> Ø de BORE_SIZES. Pelo desenho do anúncio, o eixo Plum do
    EC11 é serrilhado (~20 dentes), com crista Ø6 (+0/-0,1), fundo de dente ~Ø5,3 (estimado
    do desenho) e fenda central de ~1 mm que o deixa elástico. O furo liso precisa ficar
    entre o fundo e a crista para os dentes "morderem" o plástico; furos impressos saem
    ~0,1 mm menores que o modelo. Ø6,1 é maior que a crista e só prende por acaso.
  - Entrada cônica (LEAD_IN) no furo, para guiar o eixo e não lascar a primeira camada ao encaixar.

Os diâmetros de BORE_SIZES são ponto de partida: imprima a tira de teste e escolha o que
prende o eixo com um clique firme, sem trincar o knob.
"""
import os
import sys
import zipfile

import numpy as np
import trimesh
import manifold3d as m3d

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = os.path.join(ROOT, "hardware", "case-pehmis", "3mf", "Knob-X2.3mf")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "hardware", "knob-plum")

BORE_SIZES = (5.9,)           # furo escolhido no teste (o de 5,8 não entrou no eixo); aceita vários
FIT_TEST_SIZES = (5.5, 5.6, 5.7, 5.8, 5.9, 6.0)   # furos da tira de teste (independem de BORE_SIZES)
LEAD_IN = 0.6                  # entrada cônica a 45° na boca do furo (mm)
SEGMENTS = 128

# Geometria do furo no original (eixo Z, mm, no sistema do 3MF de origem).
CX, CY = 20.2395, -74.5488     # centro do knob
Z_BORE_END = -17.2851          # fundo fechado do furo do eixo
Z_SHOULDER = -9.4851           # degrau onde o furo liso encontra o rebaixo de Ø10
ORIG_BORE_D = 6.1
Z_BASE = -21.9851              # face de assentamento na mesa (z = 0 ao imprimir)
BASE_RED_TOL = 1e-3            # a face plana da base é vermelha no original

EPS = 0.01


def cylinder(d, z0, z1, d_top=None):
    c = m3d.Manifold.cylinder(z1 - z0, d / 2, (d_top if d_top else d) / 2, SEGMENTS)
    return c.translate([CX, CY, z0])


def load_knob():
    scene = trimesh.load(SRC)
    assert len(scene.graph.nodes_geometry) == 1, "o Knob-X2 deveria ter uma só instância"
    mesh = list(scene.geometry.values())[0]
    assert mesh.is_watertight
    return mesh


def make_knob(mesh, bore_d):
    base = m3d.Manifold(m3d.Mesh(mesh.vertices.astype(np.float32), mesh.faces.astype(np.uint32)))
    # 1) tapa o furo antigo. O tampão entra 0,05 mm no sólido do fundo e para 0,02 mm antes do degrau,
    #    para nunca coincidir com as faces originais (float32 geraria arestas não-manifold); a fresta
    #    de 0,02 mm cai dentro do cone de entrada, que a remove.
    fill = cylinder(ORIG_BORE_D + 0.4, Z_BORE_END - 0.05, Z_SHOULDER - 0.02)
    solid = base + fill
    # 2) abre o furo novo e a entrada cônica (a ponta entra no rebaixo de Ø10, que é vazio)
    cut = cylinder(bore_d, Z_BORE_END, Z_SHOULDER + EPS)
    cone = cylinder(bore_d, Z_SHOULDER - LEAD_IN, Z_SHOULDER + EPS, bore_d + 2 * (LEAD_IN + EPS))
    result = solid - cut - cone
    out = result.to_mesh()
    return trimesh.Trimesh(np.asarray(out.vert_properties)[:, :3], np.asarray(out.tri_verts))


def write_3mf(meshes, path, names=None, red_base=True, z_shift=-Z_BASE, spacing=22.0):
    """Escreve 3MF com um objeto por malha, lado a lado em X, e a face de base em vermelho,
    como no original (o trimesh perderia a cor)."""
    if isinstance(meshes, trimesh.Trimesh):
        meshes = [meshes]
    names = names or [None] * len(meshes)
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<model unit="millimeter" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" '
             'xmlns:m="http://schemas.microsoft.com/3dmanufacturing/material/2015/02">',
             ' <resources>',
             '  <m:colorgroup id="1"><m:color color="#F6F6F3FF"/><m:color color="#C43527FF"/></m:colorgroup>']
    ids = []
    for i, (mesh, name) in enumerate(zip(meshes, names)):
        oid = i + 2
        ids.append(oid)
        v = mesh.vertices.copy()
        v[:, 0] += (i - (len(meshes) - 1) / 2) * spacing
        v[:, 2] += z_shift     # knob: base em z = 0, como o <build> do original
        tri_red = (np.all(np.abs(mesh.vertices[mesh.faces][:, :, 2] - Z_BASE) < BASE_RED_TOL, axis=1)
                   if red_base else np.zeros(len(mesh.faces), bool))
        attr = f' name="{name}"' if name else ''
        lines.append(f'  <object id="{oid}" type="model"{attr}><mesh><vertices>')
        lines += [f'   <vertex x="{x:.5f}" y="{y:.5f}" z="{z:.5f}"/>' for x, y, z in v]
        lines.append('  </vertices><triangles>')
        lines += [f'   <triangle v1="{a}" v2="{b}" v3="{c}" pid="1" p1="{int(r)}"/>'
                  for (a, b, c), r in zip(mesh.faces, tri_red)]
        lines.append('  </triangles></mesh></object>')
    lines += [' </resources>',
              ' <build>' + ''.join(f'<item objectid="{oid}"/>' for oid in ids) + '</build>', '</model>']
    content_types = ('<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/'
                     'package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.'
                     'openxmlformats-package.relationships+xml"/><Default Extension="model" ContentType='
                     '"application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/></Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/'
            'package/2006/relationships"><Relationship Target="/3D/3dmodel.model" Id="rel1" Type="http://'
            'schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/></Relationships>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("3D/3dmodel.model", "\n".join(lines))


def test_strip():
    """Barra de 6 mm com um furo por diâmetro e 1..N marcas na borda; a barra imita o trecho do furo."""
    sizes = list(FIT_TEST_SIZES)
    pitch, h, thick = 12.0, 13.0, 6.0
    w = pitch * len(sizes)
    bar = m3d.Manifold.cube([w, h, thick])
    for i, d in enumerate(sizes):
        bar -= m3d.Manifold.cylinder(thick + 2, d / 2, d / 2, SEGMENTS).translate([pitch / 2 + i * pitch, h / 2, -1])
        for k in range(i + 1):   # marcas: 1 = menor furo
            bar -= m3d.Manifold.cylinder(thick + 2, 0.7, 0.7, 24).translate(
                [pitch / 2 + i * pitch + (k - i / 2) * 2.0, 1.8, -1])
    out = bar.to_mesh()
    mesh = trimesh.Trimesh(np.asarray(out.vert_properties)[:, :3], np.asarray(out.tri_verts))
    return mesh, sizes


def bore_label(sizes):
    """'5.9' para um tamanho, '5.7-5.9' para vários (usado nos nomes de arquivo)."""
    return f"{sizes[0]:.1f}" if len(sizes) == 1 else f"{sizes[0]:.1f}-{sizes[-1]:.1f}"


def report(name, mesh, ref=None):
    msg = f"{name}: watertight={mesh.is_watertight} extents={mesh.extents.round(2)} vol={mesh.volume:.0f}mm3"
    if ref is not None:
        msg += f" (delta {mesh.volume - ref.volume:+.1f}mm3 vs original)"
    print(msg)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    original = load_knob()
    knobs, names = [], []
    for d in BORE_SIZES:
        knob = make_knob(original, d)
        assert knob.is_watertight, f"furo Ø{d}: malha não fechou"
        report(f"bore {d:.1f} mm", knob, original)
        knobs.append(knob)
        names.append(f"Knob-X2_plum15_bore-{d:.1f}mm")
    path = os.path.join(OUT, f"Knob-X2_plum15_bore-{bore_label(BORE_SIZES)}mm.3mf")
    write_3mf(knobs, path, names)
    back = trimesh.load(path)
    print(os.path.basename(path), "->", len(back.geometry), "objetos:",
          all(g.is_watertight for g in back.geometry.values()))
    strip, sizes = test_strip()
    path = os.path.join(OUT, f"fit-test_{sizes[0]:.1f}-{sizes[-1]:.1f}mm.3mf")
    write_3mf(strip, path, red_base=False, z_shift=0)
    report(os.path.basename(path), trimesh.load(path, force="mesh"))
    print("furos da tira de teste (marcas 1..N):", sizes)
