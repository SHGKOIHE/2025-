import sys
from PIL import Image; import numpy as np
A = np.array(Image.open('/home/user/2025-/ace_first_front.png'))[..., 3]
out = Image.new('RGB', (900, 600))
for f in sys.argv[1:]:
    im = Image.open(f); a = np.array(im)
    print(f, im.size, im.mode, im.info.get('dpi'), 'alpha_diff', int((a[..., 3] != A).sum()), 'outside_rgb_max', int(a[a[..., 3] == 0][:, :3].max()), 'semi', int(((a[..., 3] > 0) & (a[..., 3] < 255)).sum()))
im = Image.open(sys.argv[1])
for i, c in enumerate([(255, 255, 255), (0, 0, 0)]):
    bg = Image.new('RGBA', im.size, c + (255,)); bg.alpha_composite(im); bg = bg.convert('RGB')
    out.paste(bg.crop((40, 60, 340, 360)), (0, 300*i)); out.paste(bg.crop((1380, 860, 1580, 1160)).resize((200, 300)), (300, 300*i)); out.paste(bg.crop((1380, 60, 1580, 260)).resize((300, 300)), (560, 300*i))
out.save('edge_check.png')
