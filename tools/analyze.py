"""Prepare a card: strip text, render, measure label ink boxes, list inline icon candidates."""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from strip import strip_pages, default_keep
import pymupdf as fitz
from PIL import Image
import numpy as np
S = 300/72
LABEL_WORDS = {'WEAPONS', 'RANGE', 'RUN', 'DESTROY', 'ATTACKER', 'DEFENDER', 'ACTION', 'REACTION'}

def prep(src, pages, out, keep=None):
    os.makedirs(out, exist_ok=True)
    d = fitz.open(src)
    for k, p in enumerate(pages):
        d[p].get_pixmap(dpi=300).save(f'{out}/orig_{k}.png')
    spans = []
    for b in d[pages[0]].get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for sp in l['spans']:
                spans.append(dict(font=sp['font'].split('+')[-1], size=round(sp['size']*S, 1), color='#%06x' % sp['color'],
                                  bbox=[round(v*S) for v in sp['bbox']], text=sp['text']))
    strip_pages(src, pages, f'{out}/clean.pdf', keep=keep or (lambda f, t: default_keep(f, t) and 'Scout-Regular' not in f))
    c = fitz.open(f'{out}/clean.pdf')
    for k in range(len(pages)):
        c[k].get_pixmap(dpi=300).save(f'{out}/clean_{k}.png')
    o = np.array(Image.open(f'{out}/orig_0.png').convert('RGB')).astype(int)
    cl = np.array(Image.open(f'{out}/clean_0.png').convert('RGB')).astype(int)
    diff = np.abs(o - cl).sum(2) > 60
    def ink(bb):
        x0, y0, x1, y1 = bb; x0 -= 4; y0 -= 4; x1 += 4; y1 += 4
        m = diff[y0:y1, x0:x1]; ys, xs = np.nonzero(m)
        if len(xs) == 0: return None
        return [int(x0+xs.min()), int(y0+ys.min()), int(x0+xs.max()+1), int(y0+ys.max()+1)]
    labels = {}
    for sp in spans:
        t = sp['text'].strip()
        if t in LABEL_WORDS and t not in labels:
            labels[t] = ink(sp['bbox'])
        if 'Scout-BlackItalic' in sp['font'] and sp['size'] > 44 and 'title' not in labels:
            labels['title'] = ink(sp['bbox']); labels['title_color'] = sp['color']
    # inline icon candidates: drawings in panel area, grouped
    rects = []
    for dr in c[0].get_drawings():
        r = dr['rect'] * S
        if r.x0 > 690 and 280 < r.y0 < 900 and r.width < 130 and r.height < 90:
            rects.append([r.x0, r.y0, r.x1, r.y1])
    groups = []
    for r in rects:
        for g in groups:
            if not (r[0] > g[2]+2 or r[2] < g[0]-2 or r[1] > g[3]+2 or r[3] < g[1]-2):
                g[:] = [min(g[0], r[0]), min(g[1], r[1]), max(g[2], r[2]), max(g[3], r[3])]; break
        else:
            groups.append(list(r))
    groups = [[round(v) for v in g] for g in groups]
    imgs = [(x['xref'], [round(v*S) for v in x['bbox']]) for x in c[0].get_image_info(xrefs=True)
            if (x['bbox'][2]-x['bbox'][0])*S < 130 and x['bbox'][0]*S > 690 and 280 < x['bbox'][1]*S < 900]
    info = dict(spans=spans, labels=labels, icon_groups=groups, small_imgs=imgs)
    json.dump(info, open(f'{out}/info.json', 'w'), ensure_ascii=False, indent=0)
    return info

if __name__ == '__main__':
    src, pages, out = sys.argv[1], [int(x) for x in sys.argv[2].split(',')], sys.argv[3]
    info = prep(src, pages, out)
    for sp in info['spans']:
        print(' ', sp['font'][:22], sp['size'], sp['color'], sp['bbox'], repr(sp['text']))
    print('labels', info['labels'])
    print('icons', info['icon_groups'])
    print('imgs', info['small_imgs'])
