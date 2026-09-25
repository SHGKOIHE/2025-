"""Empty Tj/TJ strings in a PDF page (recursing into Form XObjects), keeping only whitelisted text."""
import pikepdf, re

KEEP_TXT = re.compile(r'^\s*(1-3|4-6|7\+|\d+|-)\s*$')

def basefont(res, name):
    try:
        return str(res.Font[name].BaseFont)
    except Exception:
        return ''

def strip_stream(pdf, obj, res, keep, log):
    ops = pikepdf.parse_content_stream(obj)
    out = []; font = ''
    for operands, op in ops:
        o = str(op)
        if o == 'Tf':
            font = basefont(res, operands[0])
        if o in ('Tj', "'", '"', 'TJ'):
            if o == 'TJ':
                txt = ''.join(bytes(x).decode('latin1') for x in operands[0] if isinstance(x, pikepdf.String))
            else:
                txt = bytes(operands[-1]).decode('latin1')
            k = keep(font, txt)
            log.append((font, txt if 'font0' not in font else '<cid>', k))
            if not k:
                if o == 'TJ':
                    operands = [pikepdf.Array([])]
                else:
                    operands = list(operands[:-1]) + [pikepdf.String(b'')]
        if o == 'Do' and res is not None and '/XObject' in res:
            xo = res.XObject.get(operands[0])
            if xo is not None and xo.get('/Subtype') == '/Form':
                strip_stream(pdf, xo, xo.get('/Resources', res), keep, log)
        out.append((operands, op))
    data = pikepdf.unparse_content_stream(out)
    if isinstance(obj, pikepdf.Page):
        obj.Contents = pdf.make_stream(data)
    else:
        obj.write(data)

def default_keep(font, txt):
    if 'ScoutCond-RegularItalic' in font:
        return True  # big operator name
    if 'font0' in font:
        return False
    return bool(KEEP_TXT.match(txt))

def strip_pages(src, pages, dst, keep=default_keep):
    pdf = pikepdf.open(src)
    log = []
    for i in pages:
        pg = pdf.pages[i]
        strip_stream(pdf, pg, pg.Resources, keep, log)
    # keep only requested pages
    keepset = set(pages)
    for i in reversed(range(len(pdf.pages))):
        if i not in keepset:
            del pdf.pages[i]
    pdf.save(dst)
    return log

def remove_image_do(src, dst, xrefs, pages=None):
    """Remove 'Do' ops that paint image XObjects with the given object numbers (recursing into forms)."""
    pdf = pikepdf.open(src)
    def walk(obj, res):
        ops = pikepdf.parse_content_stream(obj); out = []
        for operands, op in ops:
            if str(op) == 'Do' and res is not None and '/XObject' in res:
                xo = res.XObject.get(operands[0])
                if xo is not None:
                    if xo.get('/Subtype') == '/Image' and xo.objgen[0] in xrefs:
                        continue
                    if xo.get('/Subtype') == '/Form':
                        walk(xo, xo.get('/Resources', res))
            out.append((operands, op))
        data = pikepdf.unparse_content_stream(out)
        if isinstance(obj, pikepdf.Page): obj.Contents = pdf.make_stream(data)
        else: obj.write(data)
    for i, pg in enumerate(pdf.pages):
        if pages is None or i in pages:
            walk(pg, pg.Resources)
    pdf.save(dst)
