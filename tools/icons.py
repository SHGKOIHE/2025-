import pymupdf as fitz
S = 300/72
def px2pt(r): return fitz.Rect(*[v/S for v in r])

def remove_vectors(doc, pno, rects_px, pad=9):
    pg = doc[pno]
    for r in rects_px:
        rr = fitz.Rect(r[0]-pad, r[1]-pad, r[2]+pad, r[3]+pad)
        pg.add_redact_annot(px2pt(rr), fill=False)
    pg.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE, graphics=fitz.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED, text=fitz.PDF_REDACT_TEXT_NONE)

def extract_vector_icon(src_pdf, pno, rect_px, pad=3, scale=1.0):
    """Render region with all images removed (text already stripped), alpha=True."""
    d = fitz.open(src_pdf)
    pg = d[pno]
    for x in pg.get_images(full=True):
        try: pg.delete_image(x[0])
        except Exception: pass
    r = fitz.Rect(rect_px[0]-pad, rect_px[1]-pad, rect_px[2]+pad, rect_px[3]+pad)
    pix = pg.get_pixmap(matrix=fitz.Matrix(S*scale, S*scale), clip=px2pt(r), alpha=True)
    return pix
