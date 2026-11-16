import re, sys, json
from shapely.geometry import LineString, Polygon, Point
from shapely.ops import polygonize, unary_union

import os
# Pasta com o Gerber do topo extraído (v2-gerber-top.zip). Padrão: hardware/switch-plate/gerbers-top/gerber
GERBER_DIR = os.environ.get("SOFLE_TOP_GERBER", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hardware", "switch-plate", "gerbers-top", "gerber"))
EDGE = os.path.join(GERBER_DIR, "top_plate-Edge_Cuts.gbr")
DRL = os.path.join(GERBER_DIR, "top_plate.drl")

def parse_edge(path):
    segs = []
    cur = None
    for line in open(path):
        m = re.match(r"X(-?\d+)Y(-?\d+)D0([123])\*", line.strip())
        if not m:
            continue
        x, y = int(m.group(1)) / 1e6, int(m.group(2)) / 1e6  # Gerber já usa Y para cima
        d = m.group(3)
        if d == "1" and cur is not None and (x, y) != cur:
            segs.append((cur, (x, y)))
        cur = (x, y)
    return segs

def parse_drl(path):
    holes, dia = [], {}
    tool = None
    for line in open(path):
        line = line.strip()
        m = re.match(r"T(\d+)C([\d.]+)", line)
        if m:
            dia[m.group(1)] = float(m.group(2)); continue
        m = re.match(r"T(\d+)$", line)
        if m:
            tool = m.group(1); continue
        m = re.match(r"X(-?[\d.]+)Y(-?[\d.]+)", line)
        if m and tool in dia:
            holes.append((float(m.group(1)), float(m.group(2)), dia[tool]))
    return holes

def build():
    segs = parse_edge(EDGE)
    # snap endpoints to 1 µm grid to close loops
    def snap(p):
        return (round(p[0], 3), round(p[1], 3))
    lines = [LineString([snap(a), snap(b)]) for a, b in segs]
    polys = list(polygonize(unary_union(lines)))
    polys.sort(key=lambda p: p.area, reverse=True)
    outer = Polygon(polys[0].exterior)
    inner = [Polygon(p.exterior) for p in polys[1:] if outer.contains(p.representative_point())]
    holes = parse_drl(DRL)
    return outer, inner, holes

if __name__ == "__main__":
    outer, inner, holes = build()
    minx, miny, maxx, maxy = outer.bounds
    print("outer bounds mm:", round(maxx - minx, 2), "x", round(maxy - miny, 2))
    print("inner cutouts:", len(inner))
    for p in inner:
        mrr = p.minimum_rotated_rectangle
        c = list(mrr.exterior.coords)
        import math
        e1 = math.dist(c[0], c[1]); e2 = math.dist(c[1], c[2])
        print(f"  area={p.area:7.2f}  rect={min(e1,e2):.2f}x{max(e1,e2):.2f}  verts={len(p.exterior.coords)-1}")
    print("drill holes:", holes)
