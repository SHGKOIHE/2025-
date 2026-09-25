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
