import sys
from typeset import *
from PIL import Image
import numpy as np
ALPHA = np.array(Image.open('/home/user/2025-/ace_first_front.png'))[..., 3]
WH = (255, 255, 255)
PITCH = {40: 46, 42: 48, 44: 51}

def fit_size(paras, bottom_limit, right=1460, margin=24):
    """Largest of 44/42/40 where every paragraph fits width and the last one ends >= margin above bottom_limit.
    Paragraphs after the first follow the previous one (cy = prev last line + pitch + 24) unless they carry a fixed cy."""
    for size in (44, 42, 40, 'fallback'):
        force = size == 'fallback'
        if force: size = 40
        pitch = PITCH[size]; ok = True; out = []; prev_end = None
        for p in paras:
            cy = p['cy'] if p.get('fixed_cy', True) or prev_end is None else prev_end + pitch + 24
            lines = layout(p['runs'], x_first=p['x_first'], x_rest=p['x_rest'], right=right, size=size)
            w = max(_line_w(l, size) for l in lines)
            end = cy + (len(lines)-1)*pitch
            if w > right: ok = False
            if 'limit' in p and end + size*0.55 > p['limit']: ok = False
            out.append(dict(p, size=size, cy=cy)); prev_end = end
        if force:
            print('WARNING: does not fit even at 40', [(o['cy']) for o in out], prev_end + size*0.55, bottom_limit)
            return size, out
        if ok and prev_end + size*0.55 <= bottom_limit - margin:
            return size, out

def _line_w(line, size):
    start, words = line
    word, sp, x = words[-1]
    from typeset import _word_w
    return x + _word_w(word, size, 0.0)

def build(bg_path, back, out, *, labels, title, paras, title_icon=None, team='공격팀', team_color='#3676b9', extra_titles=()):
    """labels: dict of ink boxes from original. paras: list of dict(runs, x_first, x_rest, cy, right, tracking)."""
    img = Image.open(bg_path).convert('RGBA')
    cf = gray if back else (lambda c: c)
    icf = gray_img if back else (lambda im: im)
    rep = {}
    L = labels
    def c(b): return ((b[0]+b[2])/2, (b[1]+b[3])/2)
    rep['무기'] = draw_label(img, '무기', F('Bold', 37), cf(hexc('#cacaca')), cx=c(L['WEAPONS'])[0], cy=c(L['WEAPONS'])[1])
    rep['사거리'] = draw_label(img, '사거리', F('Regular', 28), cf(hexc('#b9b8b8')), right=L['RANGE'][2], cy=c(L['RANGE'])[1])
    if 'RUN' in L:
        rep['달리기'] = draw_label(img, '달리기', F('Bold', 34), cf(hexc('#cecece')), right=L['RUN'][2], cy=c(L['RUN'])[1])
    if 'DESTROY' in L:
        rep['파괴'] = draw_label(img, '파괴', F('Bold', 34), cf(hexc('#cecece')), right=L['DESTROY'][2], cy=c(L['DESTROY'])[1])
    rep[team] = draw_label(img, team, F('Regular', 37), cf(hexc(team_color)), left=L['TEAM'][0], cy=c(L['TEAM'])[1])
    for k, word in (('ACTION', '행동'), ('ACTION2', '행동'), ('REACTION', '반응'), ('REACTION2', '반응')):
        if k in L:
            rep[k] = draw_label(img, word, F('Bold', 34), WH, cx=c(L[k])[0], cy=c(L[k])[1])
    tf = F('Bold', 56); tcx, tcy, tcol = title['cx'], title['cy'], cf(hexc(title['color']))
    if title_icon is None:
        rep['title'] = draw_label(img, title['text'], tf, tcol, cx=tcx, cy=tcy)
    else:
        b = tf.getbbox(title['text'], anchor='ls'); tw = b[2]-b[0]; ic = icf(title_icon)
        total = tw + 16 + ic.width; left = tcx - total/2
        rep['title'] = draw_label(img, title['text'], tf, tcol, left=left, cy=tcy)
        img.alpha_composite(ic, (round(left + tw + 16), round(tcy - ic.height/2)))
    for et in extra_titles:
        rep['title2'] = draw_label(img, et['text'], tf, cf(hexc(et['color'])), cx=et.get('cx', 1086), cy=et['cy'])
    for i, p in enumerate(paras):
        tr = p.get('tracking', 0.0); size = p.get('size', 40); pitch = p.get('pitch', PITCH[size])
        lines = layout(p['runs'], x_first=p['x_first'], x_rest=p['x_rest'], right=p.get('right', 1460), size=size, tracking=tr)
        ext = render_lines(img, lines, cy_first=p['cy'], pitch=pitch, size=size, tracking=tr, colorfn=cf, iconfn=icf)
        rep[f'p{i}'] = dict(size=size, pitch=pitch, lines=len(lines), maxw=round(max(e[1] for e in ext)), bottom=round(p['cy'] + (len(lines)-1)*pitch + size*0.55))
    a = np.array(img); a[..., 3] = ALPHA; a[ALPHA == 0, :3] = 0
    Image.fromarray(a, 'RGBA').save(out, dpi=(300, 300))
    return rep
