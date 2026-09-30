"""Place cards onto the Nodinod seal-sticker template (.ai = PDF, 330x480 mm, cutter reg marks at the corners).
Card art (2 mm bleed) goes on the template's '인쇄' layer, die-cut outlines (vector, CMYK magenta) on its '칼선' layer.
Cards: 120x90 mm, 2 cols x 4 rows inside the 255x385 mm work area centred between the registration marks."""
import os, sys, io
import pymupdf as fitz
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from print_a4 import ORDER
from print_layers import CARD_PX, CW, CH, BLEED, PX, outline

PT = 72 / 25.4
AREA = (37.5, 57.5, 292.5, 442.5)      # 255x385 mm, centred between the reg marks (x 30..300, y 50..450)

def ocg_xref(doc, name):
    for x, v in doc.get_ocgs().items():
        if v['name'] == name: return x
    raise KeyError(name)

def build(names, art_dir, tpl, out, cols=2, rows=4, stroke=0.25):
    doc = fitz.open(tpl)
    oc_art, oc_cut = ocg_xref(doc, '인쇄'), ocg_xref(doc, '칼선')
    per = cols * rows // 2
    npages = (len(names) + per - 1) // per
    for _ in range(npages - 1):
        doc.fullcopy_page(0)
    ax0, ay0, ax1, ay1 = AREA
    gx = ((ax1 - ax0) - cols * CW) / (cols + 1); gy = ((ay1 - ay0) - rows * CH) / (rows + 1)
    b = round(BLEED / PX)
    for pi in range(npages):
        pg = doc[pi]
        slots = []
        for n in names[pi * per:(pi + 1) * per]:
            slots += [f'{n}_front', f'{n}_back']
        for k, base in enumerate(slots):
            r, c = divmod(k, cols)
            x, y = ax0 + gx + c * (CW + gx), ay0 + gy + r * (CH + gy)
            im = Image.open(os.path.join(art_dir, base + '.png')).convert('RGB')
            im = im.crop((CARD_PX[0] - b, CARD_PX[1] - b, CARD_PX[2] + b, CARD_PX[3] + b))
            buf = io.BytesIO(); im.save(buf, 'JPEG', quality=92, dpi=(300, 300))
            pg.insert_image(fitz.Rect((x - BLEED) * PT, (y - BLEED) * PT, (x + CW + BLEED) * PT, (y + CH + BLEED) * PT),
                            stream=buf.getvalue(), oc=oc_art)
            pts = [fitz.Point(px * PT, py * PT) for px, py in outline(x, y)]
            sh = pg.new_shape(); sh.draw_polyline(pts + [pts[0]])
            sh.finish(color=(0, 1, 0, 0), width=stroke, closePath=True, fill=None, oc=oc_cut); sh.commit()
    doc.save(out, garbage=3, deflate=True)
    return npages, gx, gy

if __name__ == '__main__':
    art_dir, tpl, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    per_file = int(sys.argv[4]) if len(sys.argv) > 4 else 36
    for k in range(0, len(ORDER), per_file):
        names = ORDER[k:k + per_file]
        out = os.path.join(out_dir, f'r6_cards_nodinod_{k // per_file + 1}.pdf')
        n, gx, gy = build(names, art_dir, tpl, out)
        print(out, n, 'pages', names[0], '~', names[-1], 'gap mm', round(gx, 2), round(gy, 2), os.path.getsize(out) // 1048576, 'MB')
