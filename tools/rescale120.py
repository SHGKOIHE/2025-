"""Fit cards to 120x90 mm without cropping: fill outside-old-mask area from the source PDF render (bleed),
scale the whole card uniformly by 120/126.07, and apply the 120x90 outline (TL chamfer 20 mm, BR 15 mm) centred.
The extra 2.1 mm at top and bottom comes from the original print bleed."""
import os, sys, numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
import remask
import pymupdf as fitz

OLD = (61, 89, 1549, 1151)                      # old outline bbox (126.07 x 90 mm)
F = 120 / 126.07
W, H = 1590, 1236

def new_mask():
    # same chamfer geometry as remask, outline 1418 x 1063 px centred on the old outline centre
    cx = (OLD[0] + OLD[2] + 1) / 2; cy = (OLD[1] + OLD[3] + 1) / 2
    remask.X0 = round(cx - 709); remask.X1 = remask.X0 + 1417
    remask.Y0 = round(cy - 531.5); remask.Y1 = remask.Y0 + 1062
    return remask.mask()

def run(inputs, outdir):
    M = new_mask(); os.makedirs(outdir, exist_ok=True); docs = {}
    cx = (OLD[0] + OLD[2] + 1) / 2; cy = (OLD[1] + OLD[3] + 1) / 2
    for path in inputs:
        base = os.path.basename(path)[:-4]; name, side = base.rsplit('_', 1)
        pdf, p = remask.PAGES[name]; p += (side == 'back')
        d = docs.setdefault(pdf, fitz.open(os.path.join(remask.SRC, pdf)))
        pix = d[p].get_pixmap(dpi=300)
        ref = np.frombuffer(pix.samples, np.uint8).reshape(pix.height, pix.width, pix.n)[..., :3].astype(float)
        a = np.array(Image.open(path).convert('RGBA')).astype(float)
        al = a[..., 3:4] / 255
        full = a[..., :3] * al + ref * (1 - al)          # card art inside, PDF bleed outside
        img = Image.fromarray(np.clip(full, 0, 255).astype(np.uint8))
        sw, sh = round(W * F), round(H * F)
        small = img.resize((sw, sh), Image.LANCZOS)
        canvas = Image.fromarray(ref.astype(np.uint8))   # background for any uncovered border
        canvas.paste(small, (round(cx - cx * F), round(cy - cy * F)))
        out = np.array(canvas.convert('RGBA')); out[..., 3] = M; out[M == 0, :3] = 0
        Image.fromarray(out, 'RGBA').save(os.path.join(outdir, base + '.png'), dpi=(300, 300))
    return M

if __name__ == '__main__':
    run(sys.argv[2:], sys.argv[1])
