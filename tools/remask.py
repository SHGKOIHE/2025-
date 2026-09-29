"""Re-mask finished cards to a 120x90 mm outline (top-left chamfer 20 mm, bottom-right 15 mm, measured along the cut).
Pixels newly revealed by the smaller chamfers are filled from the 300dpi render of the source PDF page."""
import os, sys, numpy as np
from PIL import Image, ImageDraw
import pymupdf as fitz
SRC = '/tmp/claude-0/-home-user-2025-/fc4c600a-35b4-500a-a924-57931b169659/scratchpad/src'
MM = 300 / 25.4
X0, X1, Y0, Y1 = 96, 1513, 89, 1151
TLH, TLV, BRH, BRV, BL = 12.0 * MM, 16.0 * MM, 7.55 * MM, 12.96 * MM, 20

def mask():
    K = 8
    poly = [(X0 + TLH, Y0), (X1 + 1, Y0), (X1 + 1, Y1 + 1 - BRV), (X1 + 1 - BRH, Y1 + 1), (X0 + BL, Y1 + 1), (X0, Y1 + 1 - BL), (X0, Y0 + TLV)]
    big = Image.new('L', (1590 * K, 1236 * K), 0); ImageDraw.Draw(big).polygon([(x * K, y * K) for x, y in poly], fill=255)
    return np.array(big.resize((1590, 1236), Image.LANCZOS))

PAGES = {}
def add(pdf, names):
    for i, n in enumerate(names):
        if n: PAGES[n] = (pdf, 2 * i)
add('01A.pdf', ['ash', 'blitz', 'fuze', 'glaz', 'iq', 'montagne', 'sledge', 'thatcher', 'thermite', 'twitch'])
add('01B.pdf', ['bandit', 'castle', 'doc', 'jager', 'jager2', 'kapkan', 'mute', 'pulse', 'rook', 'smoke', 'tachanka_classic', 'tachanka_alternative'])
add('02_Y1.pdf', ['blackbeard', 'buck', 'capitao', 'hibana', 'hibana2', 'caveira', 'echo', 'frost', 'valkyrie'])
add('03_Y2.pdf', ['dokkaebi', 'jackal', 'ying', 'zofia', 'ela', 'lesion_first', 'lesion_second', 'mira', 'vigil'])
add('04_Y3.pdf', ['finka', 'lion', 'maverick', 'nomad', 'alibi', 'clash', 'kaid', 'maestro', 'maestro_second'])
add('05_Y4.pdf', ['amaru', 'gridlock', 'kali', 'nokk_first', 'nokk_second', 'goyo', 'mozzie', 'wamai', 'warden'])
add('06_Y5.pdf', ['ace_first', 'ace_second', 'iana', 'zero', 'aruni', 'melusi', 'oryx'])
add('07.pdf', ['flores', 'thunderbird'])

def run(inputs, outdir):
    M = mask(); os.makedirs(outdir, exist_ok=True); docs = {}
    for path in inputs:
        base = os.path.basename(path)[:-4]; name, side = base.rsplit('_', 1)
        pdf, p = PAGES[name]; p += (side == 'back')
        d = docs.setdefault(pdf, fitz.open(os.path.join(SRC, pdf)))
        pix = d[p].get_pixmap(dpi=300)
        ref = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, pix.n)[..., :3]
        a = np.array(Image.open(path).convert('RGBA'))
        rev = (M > 0) & (a[..., 3] < 255)
        a[rev, :3] = ref[rev]
        a[..., 3] = M; a[M == 0, :3] = 0
        Image.fromarray(a, 'RGBA').save(os.path.join(outdir, base + '.png'), dpi=(300, 300))
    return M

if __name__ == '__main__':
    run(sys.argv[2:], sys.argv[1])
