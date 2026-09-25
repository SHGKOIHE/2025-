import sys; sys.path.insert(0, 'lib')
from quick import *
import numpy as np
M, B = 'Medium', 'ExtraBold'; N = ' '; OR = hexc('#ec8a42'); BL = hexc('#7899ce')
ic = lambda f: Image.open(f).convert('RGBA')
# ORYX
dest, warn = ic('ox/icon_dest.png'), ic('ox/icon_warn.png')
p = [('t', ': 이동하는 동안 ORYX는 이동 경로에 있는 칸막이에 비용 없이 파괴', M, WH), ('i', dest), ('t', '행동을 수행하여 통과할 수 있습니다. 또한 ORYX는', M, WH), ('i', warn),
     ('t', '를 무시하고 파란색 진입로 공간을 사용할 수' + N + '있습니다.', M, WH)]
rep = run_card('ox', 'oryx', '리마 질주', [dict(runs=p, x_first=1023, x_rest=738, cy=461, limit=697 - 8)], 697, label_override={'ACTION': [751, 440, 843, 474]})
size = rep['p0']['size']
for k, back in ((0, False), (1, True)):
    f = f'ox/oryx_{"back" if back else "front"}.png'
    im = Image.open(f); alpha = np.array(im)[..., 3].copy()
    cf = gray if back else (lambda c: c)
    draw_label(im, '유지 단계:', F('Medium', size), cf(WH), right=950, cy=749)
    draw_label(im, '.', F('Medium', size), cf(WH), left=1073, cy=749)
    b = np.array(im); b[..., 3] = alpha; b[alpha == 0, :3] = 0
    Image.fromarray(b, 'RGBA').save(f, dpi=(300, 300))
# FLORES
dest, fire = ic('fl/icon_dest.png'), ic('fl/icon_fire.png')
p = [('t', '드론', B, BL), ('t', ' — 스캔을 완료하면, 라테로가 이동을 끝낸 공간과 그 인접 공간에서 파괴', M, WH), ('i', dest), ('t', '행동을 수행합니다. 해당 공간의 오퍼레이터는', M, WH), ('i', fire), ('t', '를' + N + '입습니다.', M, WH)]
run_card('fl', 'flores', '라테로 드론 (RCE-Ratero)', [dict(runs=p, x_first=967, x_rest=733, cy=419.5)], 677, title_icon=ic('fl/icon_title.png'), label_override={'ACTION': [796, 399, 888, 432]})
# THUNDERBIRD
dmg = ic('tb/icon_dmg.png')
p1 = [('t', '준비', B, OR), ('t', ' — 단단한 벽 섹션 3곳에 코나 스테이션을 3개까지 배치합니다.', M, WH)]
p2 = [('t', '하나 이상의 코나 스테이션이 있는 방의 오퍼레이터(공격팀 또는 방어팀)가 타격을 받을 때마다,', M, WH), ('i', dmg), ('t', '를' + N + '무시합니다.', M, WH)]
run_card('tb', 'thunderbird', '코나 스테이션', [dict(runs=p1, x_first=733, x_rest=733, cy=451), dict(runs=p2, x_first=734, x_rest=734, cy=None, fixed_cy=False)], 776,
         title_icon=ic('tb/icon_title.png'))
