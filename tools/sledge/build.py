import sys; sys.path.insert(0, '../lib')
from typeset import *
from PIL import Image
import numpy as np
ALPHA = np.array(Image.open('/home/user/2025-/ace_first_front.png'))[..., 3]

W, B, BL = 'Medium', 'ExtraBold', hexc('#7899ce')
WH = (255, 255, 255)
icon = Image.open('icon_destroy.png').convert('RGBA'); icon = icon.crop(icon.getchannel('A').getbbox())
TITLE = sys.argv[1] if len(sys.argv) > 1 else '파쇄망치 (The Caber)'
GADGET = '파쇄망치'

p1 = [('t', 'SLEDGE는 기울이기 상태에서는 ' + GADGET + '를 사용할 수 없습니다.', W, WH)]
BR = ('br',)
p2 = [('t', '배치,', B, BL), ('t', ' 얇은 벽 또는', W, BL), BR, ('t', '바리케이드 중 1개를 무시', W, BL), ('t', ' —', W, WH), BR,
      ('t', '목표 공간에서 파괴', W, WH), ('i', icon), ('t', '행동을 수행한 다음', W, WH), BR,
      ('t', '자신의 미니어처를 그곳에 놓습니다.', W, WH), BR,
      ('t', '그 후 새 위치에 인접한 공간 한 곳에서', W, WH), BR,
      ('t', '사격 및/또는 파괴', W, WH), ('i', icon), ('t', '행동을', W, WH), BR,
      ('t', '수행할 수 있습니다.', W, WH)]

def build(bg_path, back, out):
    img = Image.open(bg_path).convert('RGBA')
    cf = gray if back else (lambda c: c)
    icf = gray_img if back else (lambda im: im)
    rep = {}
    # labels
    rep['무기'] = draw_label(img, '무기', F('Bold', 37), cf(hexc('#cacaca')), cx=(579+704)/2, cy=(123+150)/2)
    rep['사거리'] = draw_label(img, '사거리', F('Regular', 28), cf(hexc('#b9b8b8')), right=844, cy=(137+161)/2)
    rep['달리기'] = draw_label(img, '달리기', F('Bold', 34), cf(hexc('#cecece')), right=1232, cy=(979+1003)/2)
    rep['파괴'] = draw_label(img, '파괴', F('Bold', 34), cf(hexc('#cecece')), right=1215, cy=(1052+1076)/2)
    rep['공격팀'] = draw_label(img, '공격팀', F('Regular', 37), cf(hexc('#3676b9')), left=346, cy=(911+946)/2)
    rep['행동'] = draw_label(img, '행동', F('Bold', 34), WH, cx=(874+966)/2, cy=534)
    rep['title'] = draw_label(img, TITLE, F('Bold', 56), cf(hexc('#7798cd')), cx=1086, cy=348)
    L1 = layout(p1, x_first=751, x_rest=751, right=1460)
    rep['p1'] = render_lines(img, L1, cy_first=417, pitch=46, colorfn=cf, iconfn=icf)
    L2 = layout(p2, x_first=1037, x_rest=801, right=1460)
    rep['p2'] = render_lines(img, L2, cy_first=534, pitch=46, colorfn=cf, iconfn=icf)
    a = np.array(img); a[..., 3] = ALPHA; a[ALPHA == 0, :3] = 0
    Image.fromarray(a, 'RGBA').save(out, dpi=(300, 300))
    return rep

if __name__ == '__main__':
    r = build('bg_0.png', False, 'sledge_front.png'); [print(k, v) for k, v in r.items()]
    build('bg_1.png', True, 'sledge_back.png')
