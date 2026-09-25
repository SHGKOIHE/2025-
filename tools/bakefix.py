import numpy as np
from PIL import Image

def remove_baked_text(clean_png, under_png, rect, out_png, thr=28, iters=400):
    """Within rect, pixels where (clean - under) is text-like are rebuilt: diff field is inpainted by diffusion
    from surrounding non-text pixels (keeps glow), then added back onto the under-layer."""
    c = np.array(Image.open(clean_png).convert('RGB')).astype(float)
    u = np.array(Image.open(under_png).convert('RGB')).astype(float)
    x0, y0, x1, y1 = rect
    D = c[y0:y1, x0:x1] - u[y0:y1, x0:x1]
    L = D.mean(2)
    # row baseline = row median; text = well above it
    base = np.median(L, axis=1, keepdims=True)
    m = L > base + thr
    # dilate mask 2px
    for _ in range(2):
        mm = m.copy(); mm[1:] |= m[:-1]; mm[:-1] |= m[1:]; mm[:, 1:] |= m[:, :-1]; mm[:, :-1] |= m[:, 1:]; m = mm
    F = D.copy(); F[m] = 0
    for _ in range(iters):
        P = np.pad(F, ((1, 1), (1, 1), (0, 0)), mode='edge')
        avg = (P[:-2, 1:-1] + P[2:, 1:-1] + P[1:-1, :-2] + P[1:-1, 2:]) / 4
        F[m] = avg[m]
    c[y0:y1, x0:x1][m] = (u[y0:y1, x0:x1] + F)[m]
    Image.fromarray(np.clip(np.round(c), 0, 255).astype(np.uint8)).save(out_png)
    return int(m.sum())

def remove_engraved_text(img_png, out_png, rects, thr=35, dil=2, ref='row'):
    """Bright letters baked into a flat region: pixels brighter than the row median by thr (dilated) are
    replaced with the row median colour of the unmasked pixels in that row."""
    a = np.array(Image.open(img_png).convert('RGB')).astype(float)
    total = 0
    for (x0, y0, x1, y1) in rects:
        R = a[y0:y1, x0:x1]; L = R.mean(2)
        base = np.median(L, axis=1, keepdims=True) if ref == 'row' else np.median(L)
        m = L > base + thr
        for _ in range(dil):
            mm = m.copy(); mm[1:] |= m[:-1]; mm[:-1] |= m[1:]; mm[:, 1:] |= m[:, :-1]; mm[:, :-1] |= m[:, 1:]; m = mm
        for y in range(R.shape[0]):
            if m[y].any():
                src = R[y][~m[y]] if (~m[y]).sum() > 3 else R[~m]
                R[y][m[y]] = np.median(src, axis=0)
        total += int(m.sum())
    Image.fromarray(np.clip(np.round(a), 0, 255).astype(np.uint8)).save(out_png)
    return total
