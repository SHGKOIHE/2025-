"""Lay out cards on A4 landscape (actual size 126x90 mm at 300dpi) with crop marks, single-sided.
Each row holds one operator: front on the left, back on the right (2 operators per sheet)."""
import os, sys
from PIL import Image, ImageDraw
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDER = ['ash', 'blitz', 'fuze', 'glaz', 'iq', 'montagne', 'sledge', 'thatcher', 'thermite', 'twitch',
         'bandit', 'castle', 'doc', 'jager', 'jager2', 'kapkan', 'mute', 'pulse', 'rook', 'smoke', 'tachanka_classic', 'tachanka_alternative',
         'blackbeard', 'buck', 'capitao', 'hibana', 'hibana2', 'caveira', 'echo', 'frost', 'valkyrie',
         'dokkaebi', 'jackal', 'ying', 'zofia', 'ela', 'lesion_first', 'lesion_second', 'mira', 'vigil',
         'finka', 'lion', 'maverick', 'nomad', 'alibi', 'clash', 'kaid', 'maestro', 'maestro_second',
         'amaru', 'gridlock', 'kali', 'nokk_first', 'nokk_second', 'goyo', 'mozzie', 'wamai', 'warden',
         'ace_first', 'ace_second', 'iana', 'zero', 'aruni', 'melusi', 'oryx', 'flores', 'thunderbird']
DPI = 300
MM = DPI / 25.4
PAGE = (round(297 * MM), round(210 * MM))
BOX = (61, 89, 1550, 1152)            # card outline inside the 1590x1236 PNG (ACE alpha bbox)
GAP = round(4 * MM)

def find(name, side):
    for d in ('output', '.'):
        p = os.path.join(ROOT, d, f'{name}_{side}.png')
        if os.path.exists(p): return p
    raise FileNotFoundError(name)

def card(path):
    im = Image.open(path).convert('RGBA')
    bg = Image.new('RGBA', im.size, (255, 255, 255, 255)); bg.alpha_composite(im)
    return bg.convert('RGB').crop(BOX)

def page(cards, back):
    pg = Image.new('RGB', PAGE, 'white'); d = ImageDraw.Draw(pg)
    cw, ch = BOX[2] - BOX[0], BOX[3] - BOX[1]
    x0 = (PAGE[0] - 2 * cw - GAP) // 2; y0 = (PAGE[1] - 2 * ch - GAP) // 2
    for i, c in enumerate(cards):
        r, col = divmod(i, 2)
        if back: col = 1 - col
        x, y = x0 + col * (cw + GAP), y0 + r * (ch + GAP)
        pg.paste(c, (x, y))
        L = round(3 * MM)
        for cx in (x, x + cw):
            for cy in (y, y + ch):
                sx = -1 if cx == x else 1; sy = -1 if cy == y else 1
                d.line([(cx + sx * 2, cy), (cx + sx * (L + 2), cy)], fill=(120, 120, 120), width=2)
                d.line([(cx, cy + sy * 2), (cx, cy + sy * (L + 2))], fill=(120, 120, 120), width=2)
    return pg

def build(names, out, quality=92):
    pages = []
    for i in range(0, len(names), 2):
        cards = []
        for n in names[i:i + 2]:
            cards += [card(find(n, 'front')), card(find(n, 'back'))]
        pages.append(page(cards, False))
    pages[0].save(out, save_all=True, append_images=pages[1:], resolution=DPI, quality=quality)
    return len(pages)

if __name__ == '__main__':
    out_dir = sys.argv[1]; per_file = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    for k in range(0, len(ORDER), per_file):
        names = ORDER[k:k + per_file]
        fn = os.path.join(out_dir, f'r6_cards_A4_{k // per_file + 1}.pdf')
        n = build(names, fn)
        print(fn, n, 'pages', names[0], '~', names[-1], os.path.getsize(fn) // 1048576, 'MB')
