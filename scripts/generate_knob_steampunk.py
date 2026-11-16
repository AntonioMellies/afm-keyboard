"""Gera o knob "steampunk" do encoder EC11 (eixo Plum 15 mm): cabeça cilíndrica serrilhada
em diamante, mais estreita que a do Knob-X2, com topo liso e borda chanfrada.

Uso (na raiz do repositório):
    pip install -r requirements.txt
    python scripts/generate_knob_steampunk.py [pasta_de_saida]

Entrada: o knob Plum de cada diâmetro, calculado em memória por generate_knob.py a partir de
hardware/case-pehmis/3mf/Knob-X2.3mf (o mesmo de Knob-X2_plum15_bore-<d>mm.3mf).
Saída padrão: hardware/knob-plum/knob-steampunk_bore-<d>mm.3mf — um objeto nomeado por diâmetro
de generate_knob.BORE_SIZES (hoje só Ø5,9). Com mais de um tamanho, cada objeto ganha 1, 2, 3...
pontos na face de baixo da haste para identificar o furo depois de impresso.

Encaixe: a parte interna (furo do eixo, entrada cônica e rebaixo de Ø10) NÃO é redesenhada.
Ela é copiada do knob de origem de cada tamanho: cavidade = cilindro Ø11 − knob de origem.
O script confere, por cortes a cada 0,05 mm, que os diâmetros internos ficaram iguais.

Externo (z = 0 é o topo do knob, que vai na mesa ao imprimir):
  - Cabeça Ø15 (era Ø17) de z 0 a 10,1 — mesma altura do original, então o knob fica na mesma
    altura acima do case.
  - Haste Ø12,6 de z 10,1 a 15,5, igual à original: é ela que entra no furo de Ø14 do topo do
    case Pehmis. Não aumente esse diâmetro.
"""
import math
import os
import sys
import zipfile

import manifold3d as m3d
import numpy as np
import trimesh

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_knob as plum  # noqa: E402  (encaixe do eixo Plum)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "hardware", "knob-plum")

BORE_SIZES = plum.BORE_SIZES

# Medidas que vêm do original e não podem mudar
HEAD_H = 10.1          # altura da cabeça (z 0 -> 10,1)
TOTAL_H = 15.5         # altura total
STEM_D = 12.6          # haste que entra no furo Ø14 do case
CAVITY_MAX_D = 10.0    # maior diâmetro interno (rebaixo); a cavidade é copiada até Ø11

# Desenho externo
HEAD_D = 15.0          # diâmetro nas cristas do serrilhado e nas faixas lisas
KNURL_DEPTH = 0.45     # profundidade do serrilhado (radial)
KNURL_N = 36           # losangos na volta
CHAMFER_TOP = 0.5      # chanfro da borda do topo
CHAMFER_BOTTOM = 0.4   # chanfro da borda de baixo da cabeça
KNURL_Z = (1.6, 9.2)   # faixa serrilhada; acima e abaixo ficam faixas lisas
KNURL_FADE = 0.35      # transição entre faixa lisa e serrilhado
GROOVES_Z = (1.05,)    # frisos em V na faixa lisa de cima
GROOVE_DEPTH = 0.3
GROOVE_W = 0.5
MARK_D = 0.8           # pontos de identificação na face de baixo da haste
MARK_DEPTH = 0.3

SEG_THETA = KNURL_N * 8    # resolução angular da cabeça
DZ = 0.05                  # resolução vertical da cabeça
SEGMENTS = 128


def to_manifold(mesh):
    return m3d.Manifold(m3d.Mesh(mesh.vertices.astype(np.float32), mesh.faces.astype(np.uint32)))


def to_trimesh(man):
    out = man.to_mesh()
    return trimesh.Trimesh(np.asarray(out.vert_properties)[:, :3], np.asarray(out.tri_verts))


def head_radius(theta, z):
    """Raio da cabeça em (ângulo, altura): faixas lisas, frisos, chanfros e serrilhado diamante."""
    r_max = HEAD_D / 2
    r = np.full_like(z, r_max)
    # serrilhado diamante: duas famílias de sulcos helicoidais a ±45°
    pitch = 2 * math.pi * r_max / KNURL_N
    s = theta * r_max
    fu = np.mod((s + z) / pitch, 1.0) - 0.5
    fv = np.mod((s - z) / pitch, 1.0) - 0.5
    peak = 1.0 - 2.0 * np.maximum(np.abs(fu), np.abs(fv))      # 1 no centro do losango, 0 no sulco
    z0, z1 = KNURL_Z
    w = np.clip(np.minimum(z - z0, z1 - z) / KNURL_FADE, 0.0, 1.0)
    r -= KNURL_DEPTH * (1.0 - peak) * w
    for zg in GROOVES_Z:                                          # frisos em V
        r -= GROOVE_DEPTH * np.clip(1.0 - np.abs(z - zg) / (GROOVE_W / 2), 0.0, 1.0)
    r = np.minimum(r, r_max - CHAMFER_TOP + z)                    # chanfro do topo
    r = np.minimum(r, r_max - CHAMFER_BOTTOM + (HEAD_H - z))      # chanfro de baixo
    return r


def make_head():
    """Sólido da cabeça como superfície de revolução com relevo, fechada no topo e na base."""
    zs = np.linspace(0.0, HEAD_H, int(round(HEAD_H / DZ)) + 1)
    th = np.linspace(0.0, 2 * math.pi, SEG_THETA, endpoint=False)
    T, Z = np.meshgrid(th, zs)                 # linhas = z, colunas = ângulo
    R = head_radius(T, Z)
    verts = np.column_stack([(R * np.cos(T)).ravel(), (R * np.sin(T)).ravel(), Z.ravel()])
    nz, nt = Z.shape
    idx = np.arange(nz * nt).reshape(nz, nt)
    a, b = idx[:-1, :], np.roll(idx[:-1, :], -1, axis=1)
    c, d = idx[1:, :], np.roll(idx[1:, :], -1, axis=1)
    faces = [np.column_stack([a.ravel(), c.ravel(), b.ravel()]),
             np.column_stack([b.ravel(), c.ravel(), d.ravel()])]
    top, bot = len(verts), len(verts) + 1      # centros das tampas
    verts = np.vstack([verts, [[0, 0, 0], [0, 0, HEAD_H]]])
    ring0, ring1 = idx[0], idx[-1]
    faces.append(np.column_stack([np.full(nt, top), ring0, np.roll(ring0, -1)]))
    faces.append(np.column_stack([np.full(nt, bot), np.roll(ring1, -1), ring1]))
    mesh = trimesh.Trimesh(verts, np.vstack(faces), process=True)
    if mesh.volume < 0:
        mesh.invert()
    assert mesh.is_watertight, "cabeça: malha não fechou"
    return to_manifold(mesh)


def cylinder(d, z0, z1, d_top=None, seg=SEGMENTS):
    return m3d.Manifold.cylinder(z1 - z0, d / 2, (d_top if d_top else d) / 2, seg).translate([0, 0, z0])


def make_outer():
    return make_head() + cylinder(STEM_D, HEAD_H - 0.2, TOTAL_H)   # topo (z = 0) liso


def load_source(original, d):
    """Knob Plum do diâmetro d, centrado na origem, com o topo em z = 0 (como é impresso)."""
    mesh = plum.make_knob(original, d)
    assert mesh.is_watertight, f"knob Plum Ø{d}: malha não fechou"
    mesh.apply_translation([-plum.CX, -plum.CY, -plum.Z_BASE])
    return mesh


def make_knob(src_mesh, n_marks, outer):
    cavity = cylinder(CAVITY_MAX_D + 1.0, -0.5, TOTAL_H + 0.5) - to_manifold(src_mesh)
    knob = outer - cavity
    # pontos de identificação na face de baixo da haste (anel entre Ø10 e Ø12,6)
    r_mark = (CAVITY_MAX_D + STEM_D) / 4
    for k in range(n_marks):
        ang = math.radians(90 + (k - (n_marks - 1) / 2) * 30)
        knob -= cylinder(MARK_D, TOTAL_H - MARK_DEPTH, TOTAL_H + 1, seg=24).translate(
            [r_mark * math.cos(ang), r_mark * math.sin(ang), 0])
    return to_trimesh(knob)


def inner_profile(mesh, r_lim):
    """Diâmetros dos contornos internos (r < r_lim) a cada 0,05 mm, em toda a altura."""
    prof = {}
    for z in np.arange(0.025, TOTAL_H, 0.05):
        s = mesh.section(plane_origin=[0, 0, z], plane_normal=[0, 0, 1])
        ds = []
        if s is not None:
            for loop in s.discrete:
                p = np.asarray(loop)[:, :2]
                r = np.hypot(p[:, 0], p[:, 1])
                if r.max() < r_lim:
                    ds.append(round(2 * r.mean(), 2))
        prof[round(z, 3)] = sorted(ds)
    return prof


def write_3mf(meshes, names, path, spacing=20.0):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<model unit="millimeter" xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02">',
             ' <resources>']
    for i, (mesh, name) in enumerate(zip(meshes, names)):
        v = mesh.vertices + [(i - (len(meshes) - 1) / 2) * spacing, 0, 0]
        lines.append(f'  <object id="{i + 1}" type="model" name="{name}"><mesh><vertices>')
        lines += [f'   <vertex x="{x:.5f}" y="{y:.5f}" z="{z:.5f}"/>' for x, y, z in v]
        lines.append('  </vertices><triangles>')
        lines += [f'   <triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in mesh.faces]
        lines.append('  </triangles></mesh></object>')
    lines.append(' </resources>')
    lines.append(' <build>' + ''.join(f'<item objectid="{i + 1}"/>' for i in range(len(meshes))) + '</build>')
    lines.append('</model>')
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


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    outer = make_outer()
    original = plum.load_knob()
    knobs, names = [], []
    for n, d in enumerate(BORE_SIZES, start=1):
        src = load_source(original, d)
        knob = make_knob(src, n if len(BORE_SIZES) > 1 else 0, outer)
        assert knob.is_watertight, f"furo Ø{d}: malha não fechou"
        # o encaixe precisa ser idêntico ao do knob de origem
        a, b = inner_profile(src, CAVITY_MAX_D / 2 + 0.05), inner_profile(knob, CAVITY_MAX_D / 2 + 0.05)
        diff = [z for z in a if a[z] != b[z]]
        assert not diff, f"furo Ø{d}: encaixe diferente do original em z = {diff[:5]}"
        print(f"bore {d:.1f} mm: watertight, extents={knob.extents.round(2)}, "
              f"vol={knob.volume:.0f} mm3, encaixe igual ao original em {len(a)} cortes")
        knobs.append(knob)
        marks = f"_{n}-ponto{'s' if n > 1 else ''}" if len(BORE_SIZES) > 1 else ""
        names.append(f"knob-steampunk_bore-{d:.1f}mm{marks}")
    path = os.path.join(OUT, f"knob-steampunk_bore-{plum.bore_label(BORE_SIZES)}mm.3mf")
    write_3mf(knobs, names, path)
    back = trimesh.load(path)
    print(os.path.basename(path), "->", len(back.geometry), "objetos")
