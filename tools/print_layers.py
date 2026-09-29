"""Print-shop PDF: card art with 2 mm bleed on layer '인쇄', die-cut outline as a vector path on layer '칼선'.
Also writes a cut-line-only PDF. Page 255x385 mm, 2 cols x 4 rows of 120x90 mm cards (front left, back right)."""
import os, sys, io
import pymupdf as fitz
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from print_a4 import ORDER

PT = 72 / 25.4
PX = 25.4 / 300                                  # mm per px at 300 dpi
CARD_PX = (96, 89, 1514, 1152)                   # 120x90 mm card box inside the 1590x1236 art
CW, CH = (CARD_PX[2] - CARD_PX[0]) * PX, (CARD_PX[3] - CARD_PX[1]) * PX
TLH, TLV, BRH, BRV, BL = 12.0, 16.0, 7.55, 12.96, 20 * PX
BLEED = 2.0

def outline(x, y):
    return [(x + TLH, y), (x + CW, y), (x + CW, y + CH - BRV), (x + CW - BRH, y + CH), (x + BL, y + CH), (x, y + CH - BL), (x, y + TLV)]

def build(names, art_dir, out, cut_out, page_mm=(255, 385), cols=2, rows=4, gap=5.0, stroke=0.25, color=(1, 0, 1)):
    doc, cut = fitz.open(), fitz.open()
    oc_art = doc.add_ocg('인쇄', on=True); oc_cut = doc.add_ocg('칼선', on=True)
    W, H = page_mm
    x0 = (W - cols * CW - (cols - 1) * gap) / 2; y0 = (H - rows * CH - (rows - 1) * gap) / 2
    per = cols * rows // 2
    b = round(BLEED / PX)
    for i in range(0, len(names), per):
        pg = doc.new_page(width=W * PT, height=H * PT); cp = cut.new_page(width=W * PT, height=H * PT)
        slots = []
        for n in names[i:i + per]:
            slots += [f'{n}_front', f'{n}_back']
        for k, base in enumerate(slots):
            r, c = divmod(k, cols)
            x, y = x0 + c * (CW + gap), y0 + r * (CH + gap)
            im = Image.open(os.path.join(art_dir, base + '.png')).convert('RGB')
            im = im.crop((CARD_PX[0] - b, CARD_PX[1] - b, CARD_PX[2] + b, CARD_PX[3] + b))
            buf = io.BytesIO(); im.save(buf, 'JPEG', quality=92, dpi=(300, 300))
            rect = fitz.Rect((x - BLEED) * PT, (y - BLEED) * PT, (x + CW + BLEED) * PT, (y + CH + BLEED) * PT)
            pg.insert_image(rect, stream=buf.getvalue(), oc=oc_art)
            pts = [fitz.Point(px * PT, py * PT) for px, py in outline(x, y)]
            for p in (pg, cp):
                sh = p.new_shape(); sh.draw_polyline(pts + [pts[0]])
                sh.finish(color=color, width=stroke, closePath=True, fill=None, oc=oc_cut if p is pg else 0); sh.commit()
    doc.save(out, garbage=3, deflate=True); cut.save(cut_out, garbage=3, deflate=True)
    return doc.page_count

if __name__ == '__main__':
    art_dir, out_dir = sys.argv[1], sys.argv[2]
    per_file = int(sys.argv[3]) if len(sys.argv) > 3 else 36
    for k in range(0, len(ORDER), per_file):
        names = ORDER[k:k + per_file]; j = k // per_file + 1
        out = os.path.join(out_dir, f'r6_cards_255x385_{j}.pdf'); cut = os.path.join(out_dir, f'r6_cutline_255x385_{j}.pdf')
        n = build(names, art_dir, out, cut)
        print(out, n, 'pages', names[0], '~', names[-1], os.path.getsize(out) // 1048576, 'MB')
