from PIL import Image, ImageDraw, ImageFont
import numpy as np
FD = '/tmp/claude-0/-home-user-2025-/fc4c600a-35b4-500a-a924-57931b169659/scratchpad/fonts/'
_cache = {}
def F(w, size):
    k = (w, size)
    if k not in _cache:
        _cache[k] = ImageFont.truetype(FD + f'Pretendard-{w}.otf', size)
    return _cache[k]

def hexc(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def gray(c):
    g = round(0.3*c[0] + 0.59*c[1] + 0.11*c[2]); return (g, g, g)

def gray_img(im):
    a = np.array(im.convert('RGBA')).astype(float)
    g = np.clip(np.round(0.3*a[..., 0] + 0.59*a[..., 1] + 0.11*a[..., 2]), 0, 255)
    a[..., 0] = a[..., 1] = a[..., 2] = g
    return Image.fromarray(a.astype(np.uint8), 'RGBA')

def hangul_center(font):
    """offset from baseline (anchor 'ls') to ink vertical center of typical Hangul."""
    b = font.getbbox('가나다한글', anchor='ls')
    return (b[1] + b[3]) / 2

def ink_box(text, font, anchor='ls'):
    return font.getbbox(text, anchor=anchor)

def draw_label(img, text, font, color, *, cx=None, right=None, left=None, cy):
    """Place text so that its ink box aligns: center x / right edge / left edge; ink center y = cy."""
    d = ImageDraw.Draw(img)
    b = font.getbbox(text, anchor='ls')
    w = b[2] - b[0]
    if cx is not None: x = cx - w/2 - b[0]
    elif right is not None: x = right - b[2]
    else: x = left - b[0]
    y = cy - (b[1] + b[3]) / 2
    d.text((x, y), text, font=font, fill=color, anchor='ls')
    return (x + b[0], y + b[1], x + b[2], y + b[3])

# ---- rich paragraph -------------------------------------------------------
# runs: list of ('t', text, weight, color) or ('i', PIL image)
# spaces are break opportunities; icons are glued to neighbouring words (gap 8px).
ICON_GAP = 8

def _atoms(runs, size):
    """Split into unbreakable words; each word is a list of pieces. A space ends a word."""
    words = [[]]; spaces_after = []
    for r in runs:
        if r[0] == 'i':
            words[-1].append(('i', r[1]))
            continue
        if r[0] == 'br':
            spaces_after.append('BR'); words.append([])
            continue
        _, text, w, col = r
        parts = text.split(' ')
        for k, p in enumerate(parts):
            if k > 0:
                spaces_after.append((w, col))
                words.append([])
            if p:
                words[-1].append(('t', p, w, col))
    spaces_after.append(None)
    return [x for x in zip(words, spaces_after) if x[0]]

def _piece_w(p, size, tracking):
    if p[0] == 'i': return p[1].width
    f = F(p[2], size)
    return f.getlength(p[1]) + tracking * len(p[1])

def _word_w(word, size, tracking):
    w = 0; prev = None
    for p in word:
        if prev is not None and (p[0] == 'i' or prev[0] == 'i'): w += ICON_GAP
        w += _piece_w(p, size, tracking); prev = p
    return w

def layout(runs, *, x_first, x_rest, right, size=40, tracking=0.0, forced_breaks=()):
    """Greedy wrap. forced_breaks: indexes of words before which a new line starts."""
    atoms = _atoms(runs, size)
    lines = []; cur = []; x = x_first; start = x_first
    for idx, (word, sp) in enumerate(atoms):
        ww = _word_w(word, size, tracking)
        spw = 0; forced = False
        if cur:
            psp = cur[-1][1]
            forced = psp == 'BR'
            spw = F(psp[0], size).getlength(' ') + tracking if psp and not forced else 0
        if cur and (x + spw + ww > right or idx in forced_breaks or forced):
            lines.append((start, cur)); cur = []; start = x = x_rest; spw = 0
        x += spw
        cur.append((word, sp, x)); x += ww
    if cur: lines.append((start, cur))
    return lines

def render_lines(img, lines, *, cy_first, pitch, size=40, tracking=0.0, colorfn=lambda c: c, iconfn=lambda im: im):
    d = ImageDraw.Draw(img)
    ref = hangul_center(F('Medium', size))
    extents = []
    for li, (start, words) in enumerate(lines):
        cy = cy_first + li * pitch
        base = cy - ref
        maxx = 0
        for word, sp, x in words:
            prev = None
            for p in word:
                if prev is not None and (p[0] == 'i' or prev[0] == 'i'): x += ICON_GAP
                if p[0] == 'i':
                    ic = iconfn(p[1])
                    img.alpha_composite(ic, (round(x), round(cy - ic.height/2)))
                    x += ic.width
                else:
                    f = F(p[2], size)
                    col = colorfn(p[3])
                    if tracking == 0:
                        d.text((x, base), p[1], font=f, fill=col, anchor='ls')
                        x += f.getlength(p[1])
                    else:
                        for ch in p[1]:
                            d.text((x, base), ch, font=f, fill=col, anchor='ls'); x += f.getlength(ch) + tracking
                prev = p
            maxx = max(maxx, x)
            # space coloring irrelevant (invisible)
        extents.append((start, maxx))
    return extents
