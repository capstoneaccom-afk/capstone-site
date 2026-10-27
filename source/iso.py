import math
def iso_svg(cubes, tone, N=3, H=3, s=40):
    a = s*math.cos(math.pi/6); b = s/2; cx = 120; cy = 10 + H*s
    def P(x, y, z): return (cx + (x - y)*a, cy + (x + y)*b - z*s)
    def pts(*ps): return ' '.join(f'{p[0]:.1f},{p[1]:.1f}' for p in ps)
    out = []
    # boîte englobante (hexagone) et sol quadrillé
    box = [P(0,0,H), P(N,0,H), P(N,0,0), P(N,N,0), P(0,N,0), P(0,N,H)]
    out.append(f'<polygon class="iso-box" points="{pts(*box)}"/>')
    out.append(f'<polyline class="iso-box" points="{pts(P(0,0,H), P(0,0,0))}"/>')
    out.append(f'<polyline class="iso-box" points="{pts(P(0,0,0), P(N,0,0))}"/><polyline class="iso-box" points="{pts(P(0,0,0), P(0,N,0))}"/>')
    for i in range(1, N):
        out.append(f'<polyline class="iso-grid" points="{pts(P(i,0,0), P(i,N,0))}"/><polyline class="iso-grid" points="{pts(P(0,i,0), P(N,i,0))}"/>')
    # cubes, du fond vers l'avant
    for k, (x, y, z) in enumerate(sorted(cubes, key=lambda c: (c[0]+c[1], c[2]))):
        top = pts(P(x,y,z+1), P(x+1,y,z+1), P(x+1,y+1,z+1), P(x,y+1,z+1))
        right = pts(P(x+1,y,z), P(x+1,y+1,z), P(x+1,y+1,z+1), P(x+1,y,z+1))
        left = pts(P(x,y+1,z), P(x+1,y+1,z), P(x+1,y+1,z+1), P(x,y+1,z+1))
        hatch = ''.join(f'<polyline points="{pts(P(x, y+1, z + t/8), P(x+1, y+1, z + t/8))}"/>' for t in range(1, 8))
        out.append(f'<g class="cube" style="--k:{k}"><polygon class="f-top" points="{top}"/><polygon class="f-right" points="{right}"/><polygon class="f-left" points="{left}"/><g class="hatch">{hatch}</g></g>')
    return f'<svg class="iso {tone}" viewBox="0 0 240 262" aria-hidden="true">{"".join(out)}</svg>'

ISO_BUILD = [(0,2,0), (1,2,0), (1,2,1), (2,2,0), (2,2,1), (2,2,2)]
ISO_ADVISE = [(0,0,0),(1,0,0),(2,0,0),(0,1,0),(1,1,0),(2,1,0),(0,2,0),(1,2,0),(2,2,0),(0,0,1),(1,0,1),(0,1,1),(2,0,1),(0,0,2),(1,0,2),(0,1,2),(2,1,1),(0,2,1)]

# ---------- Du plan au volume (piste D) ----------
def plan_svg(mode, tone):
    C = math.cos(math.pi/6)
    def P(u, v, z=0, cx=120, cy=150): return (cx + (u - v)*C, cy + (u + v)*0.5 - z)
    def pts(ps): return ' '.join(f'{x:.1f},{y:.1f}' for x, y in ps)
    def vol(rects, h, k, cls):
        pl, wl, rf = '', '', ''
        for (u0, v0, u1, v1) in rects:
            pl += f'<polygon class="pv-plan" points="{pts([P(u0,v0), P(u1,v0), P(u1,v1), P(u0,v1)])}"/>'
            right = [P(u1, v0), P(u1, v1), P(u1, v1, h), P(u1, v0, h)]
            left = [P(u0, v1), P(u1, v1), P(u1, v1, h), P(u0, v1, h)]
            hatch = ''.join(f'<line x1="{P(u0, v1, h*i/7)[0]:.1f}" y1="{P(u0, v1, h*i/7)[1]:.1f}" x2="{P(u1, v1, h*i/7)[0]:.1f}" y2="{P(u1, v1, h*i/7)[1]:.1f}"/>' for i in range(1, 7))
            wl += f'<polygon class="pv-wall" points="{pts(right)}"/><polygon class="pv-wall" points="{pts(left)}"/><g class="pv-hatch">{hatch}</g>'
            rf += f'<polygon class="pv-roof" points="{pts([P(u0,v0,h), P(u1,v0,h), P(u1,v1,h), P(u0,v1,h)])}"/>'
        return f'<g class="pv-vol {cls}" style="--k:{k}"><g class="pv-planl">{pl}</g><g class="pv-rise">{wl}{rf}</g></g>'
    grid = ''.join(f'<polyline class="pv-grid" points="{pts([P(i,-90), P(i,90)])}"/><polyline class="pv-grid" points="{pts([P(-90,i), P(90,i)])}"/>' for i in range(-90, 91, 30))
    if mode == 'build':
        body = vol([(-60, -20, 0, 50)], 30, 0, 'a') + vol([(0, -50, 50, 20)], 30, 1, 'b')
    else:
        body = vol([(-70, -10, 0, 60)], 34, 0, 'a base') + vol([(-10, -70, 50, 0)], 70, 1, 'b tall') + vol([(10, 10, 70, 70)], 22, 2, 'c')
    return f'<svg class="iso pv {tone} {mode}" viewBox="0 0 240 262" aria-hidden="true">{grid}{body}</svg>'
